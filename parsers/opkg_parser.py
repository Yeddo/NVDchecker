import re

def parse_opkg(output_file):
    packages = []
    with open(output_file, "r") as file:
        for line in file:
            match = re.match(r'^(\S+)\s+-\s+(\S+)$', line.strip())
            if match:
                package_name, package_version = match.groups()
                packages.append((package_name, package_version))
    return packages
