import argparse
from parsers import parse_rpm, parse_dpkg, parse_opkg
from nvd_lookup import nvd_lookup
from excel_output import create_excel_output

def main():
    parser = argparse.ArgumentParser(description="Package Manager CVE Lookup Tool")
    parser.add_argument("--input", required=True, help="Input file with package manager output")
    parser.add_argument("--output", required=True, help="Output Excel file")
    parser.add_argument("--manager", required=True, choices=["rpm", "dpkg", "opkg"], help="Package manager type")
    parser.add_argument("--api_key", help="NVD API key (optional)")
    
    args = parser.parse_args()

    # Parse the package manager output
    if args.manager == "rpm":
        packages = parse_rpm(args.input)
    elif args.manager == "dpkg":
        packages = parse_dpkg(args.input)
    elif args.manager == "opkg":
        packages = parse_opkg(args.input)
    
    # Lookup CVEs and gather results
    results = []
    for package_name, package_version in packages:
        cve_items = nvd_lookup(package_name, package_version, args.api_key)
        if cve_items:
            for cve_item in cve_items:
                cve_id = cve_item["cve"]["CVE_data_meta"]["ID"]
                cvss_score = cve_item["impact"].get("baseMetricV3", {}).get("cvssV3", {}).get("baseScore", "N/A")
                published_date = cve_item["publishedDate"]
                description = cve_item["cve"]["description"]["description_data"][0]["value"]
                results.append([package_name, package_version, cve_id, cvss_score, published_date, description])
        else:
            results.append([package_name, package_version, "None Found"])
    
    # Write results to Excel
    create_excel_output(args.output, results)

if __name__ == "__main__":
    main()
