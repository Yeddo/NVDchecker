import requests
import time
import json            # Importing json for handling JSON exceptions
from tqdm import tqdm  # Progress bar library
import sys             # For controlling output stream

def nvd_search(packages, api_key=None):
    cve_results = []
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    # List to collect log messages so we don't interfere with tqdm
    log_messages = []
    headers = {}

    # Wrapping the loop with tqdm for progress display
    with tqdm(total=len(packages), desc="Querying NVD for CVEs", unit="package", dynamic_ncols=True, leave=True, file=sys.stdout) as pbar:
        for package_name, package_version in packages:
            # Construct the CPE string for the given package name and version
            cpe_name = f"cpe:2.3:a:*:{package_name}:{package_version}:*:*:*:*:*:*:*"
            # https://nvd.nist.gov/developers/vulnerabilities
            url = f"{base_url}?virtualMatchString={cpe_name}"

            try:
                # If you have an API Key. Do yourself a favor and get/use one.
                if api_key:
                    headers['apiKey'] = api_key
                    response = requests.get(url, headers=headers)
                else:
                    time.sleep(6) # Rate limiting for anonymous API usage
                    response = requests.get(url)
            except requests.exceptions.RequestException as e:
                log_messages.append(f"Error while requesting {package_name}-{package_version}: {e}")
                pbar.update(1)
                continue

            # Handle different response codes, including 404
            if response.status_code == 200:
                try:
                    # Parse the CVE response for vulnerabilities
                    vulnerabilities = response.json().get("vulnerabilities", [])

                    if not vulnerabilities:
                        # If no vulnerabilities are found, log it
                        cve_results.append((package_name, package_version, "No vulnerabilities found", "-", "-", "-"))
                    else:
                        # Iterate over the vulnerabilities and extract relevant CVE information
                        for vuln_item in vulnerabilities:
                            cve = vuln_item.get("cve", {})
                            cve_id = cve.get("id", "Unknown CVE ID")
                            description = cve.get("descriptions", [{}])[0].get("value", "No description available")
                            
                            # Extract CVSS score
                            cvss_v3_metrics = cve.get("metrics", {}).get("cvssMetricV31", [{}])
                            cvss_score = cvss_v3_metrics[0].get("cvssData", {}).get("baseScore", "Not Provided")
                            
                            # Get the publish date of the vulnerability
                            published_date = cve.get("publishedDate", "Unknown publish date")

                            # Append the parsed CVE data to the results list
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
