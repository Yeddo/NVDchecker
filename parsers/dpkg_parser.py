import re

def parse_dpkg(output_file):
    packages = []
    with open(output_file, "r") as file:
        for line in file:
            # Seems to work ok for now until I figure out something more accurate.
            #(?:\d+:)?: This part matches the optional number and colon (e.g., 1:). It ignores this in the final result.
            #([\d\.]+): This captures the version part after the colon, ensuring all digits and periods (e.g., 6.7, 2.39.3, etc.) are kept intact.
            match = re.match(r'^(\S+)\s+-\s+(?:\d+:)?([\d\.]+)', line.strip())
            if match:
                package_name, package_version = match.groups()
                packages.append((package_name, package_version))
    return packages
