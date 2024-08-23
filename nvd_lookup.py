import requests
import time

def nvd_search(packages, api_key=None):
    cve_results = []
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    
    for package_name, package_version in packages:
        if api_key:
            url = f"{base_url}?apikey={api_key}&cpeMatchString=cpe:2.3:a:*:{package_name}:{package_version}"
        else:
            url = f"{base_url}?cpeMatchString=cpe:2.3:a:*:{package_name}:{package_version}"
            time.sleep(6) # Rate limiting for anonymous API usage

        response = requests.get(url)
        if response.status_code == 200:
            cve_items = response.json().get("result", {}).get("CVE_Items", [])
            for cve_item in cve_items:
                cve_id = cve_item["cve"]["CVE_data_meta"]["ID"]
                description = cve_item["cve"]["description"]["description_data"][0]["value"]
                cvss_score = cve_item["impact"].get("baseMetricV3", {}).get("cvssV3", {}).get("baseScore", "Not Provided")
                published_date = cve_item["publishedDate"]
                cve_results.append((package_name, package_version, cve_id, cvss_score, published_date, description))
        else:
            cve_results.append((package_name, package_version, "Error", response.status_code, response.reason, ""))
    
    return cve_results
