import re

def parse_opkg(output_file):
    packages = []
    with open(output_file, "r") as file:
        for line in file:
            
            # ^([a-zA-Z0-9\+\.\-]+)\s*-\s*: This part matches the package name. It includes letters, numbers, plus signs, dots, and hyphens.
            # ([0-9a-zA-Z\.\+]+): This part matches the version number, which may include digits, letters, periods, and plus signs.
            match = re.match(r'^([a-zA-Z0-9\+\.\-]+)\s*-\s*([0-9a-zA-Z\.\+]+)', line.strip())
            
            if match:
                package_name, package_version = match.groups()
                packages.append((package_name, package_version))
    return packages
