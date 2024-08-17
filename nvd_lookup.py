import requests
import time

def nvd_lookup(package_name, package_version, api_key=None):
    if api_key:
        url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?apikey={api_key}&cpeMatchString=cpe:2.3:a:*:{package_name}:{package_version}"
    else:
        url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:2.3:a:*:{package_name}:{package_version}"
        time.sleep(6)  # API rate limiting

    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("result", {}).get("CVE_Items", [])
    else:
        return None, response.status_code, response.reason
