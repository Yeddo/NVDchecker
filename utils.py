import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="CVE Scanner")
    parser.add_argument("--package-manager", required=True, choices=["dpkg", "rpm", "opkg"], help="Specify the package manager")
    parser.add_argument("--input-file", required=True, help="File containing the package listing")
    parser.add_argument("--output-file", default="cve_report.xlsx", help="Output Excel file")
    parser.add_argument("--api-key", help="NVD API key (optional)")
    return parser.parse_args()
