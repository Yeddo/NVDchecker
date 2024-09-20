import requests
import time
import json  # Importing json for handling JSON exceptions
from tqdm import tqdm  # Progress bar library
import sys  # For controlling output stream

def nvd_search(packages, api_key=None):
    cve_results = []
    base_url = "https://services.nvd.nist.gov/rest/json/cpematch/2.0"

    # List to collect log messages so we don't interfere with tqdm
    log_messages = []

    # Wrapping the loop with tqdm for progress display
    with tqdm(total=len(packages), desc="Querying NVD for CVEs", unit="package", dynamic_ncols=True, leave=True, file=sys.stdout) as pbar:
        for package_name, package_version in packages:
            # Format the CPE string with the proper API parameters
            cpe_name = f"cpe:2.3:a:*:{package_name}:{package_version}"

            # Construct the URL with or without the API key
            if api_key:
                url = f"{base_url}?apiKey={api_key}&cpeName={cpe_name}"
            else:
                url = f"{base_url}?cpeName={cpe_name}"
                time.sleep(6)  # Rate limiting for anonymous API usage

            try:
                response = requests.get(url)
            except requests.exceptions.RequestException as e:
                log_messages.append(f"Error while requesting {package_name}-{package_version}: {e}")
                pbar.update(1)
                continue

            # Handle different response codes, including 404
            if response.status_code == 200:
                try:
                    # Parse the CPE match response
                    cpe_matches = response.json().get("matches", [])

                    # Iterate over CPE matches to extract CVE information
                    for match in cpe_matches:
                        vulnerabilities = match.get("vulnerabilities", [])
                        for vuln in vulnerabilities:
                            cve_id = vuln.get("cve", {}).get("id", "Unknown CVE ID")
                            description = vuln.get("description", "No description available")
                            cvss_v3_metrics = vuln.get("metrics", {}).get("cvssMetricV31", [{}])
                            cvss_score = cvss_v3_metrics[0].get("cvssData", {}).get("baseScore", "Not Provided")
                            published_date = vuln.get("published", "Unknown publish date")

                            cve_results.append((package_name, package_version, cve_id, cvss_score, published_date, description))

                except json.JSONDecodeError:
                    log_messages.append(f"JSONDecodeError: Failed to decode response for {package_name}-{package_version}")
            elif response.status_code == 404:
                log_messages.append(f"404 Error: No vulnerabilities found for {package_name}-{package_version}")
            else:
                log_messages.append(f"Error: Received status code {response.status_code} for {package_name}-{package_version} - Reason: {response.reason}")

            # Update progress bar after each iteration
            pbar.update(1)

    # After the progress bar has finished, print any log messages
    if log_messages:
        sys.stdout.write("\n".join(log_messages) + "\n")

    return cve_results
