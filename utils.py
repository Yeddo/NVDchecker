import argparse
import sys
import time

def parse_args():
    parser = argparse.ArgumentParser(description="Snail CVE Scanner")
    parser.add_argument("--package-manager", required=True, choices=["dpkg", "rpm", "opkg"], help="Specify the package manager")
    parser.add_argument("--input-file", required=True, help="File containing the package listing")
    parser.add_argument("--output-file", default="cve_report.xlsx", help="Output Excel file")
    parser.add_argument("--api-key", help="NVD API key (optional)")
    return parser.parse_args()

# Function to print text slowly. Fancy!
def delay_print(s):
    for c in s:
        # Two tricks here ...
        sys.stdout.write(c) # 1. you need to use a stream to get everything in the right place.
        sys.stdout.flush()  # 2. you also need to flush the stream buffer.
        time.sleep(0.05)    # Adjust to speed up/slow down
        
        