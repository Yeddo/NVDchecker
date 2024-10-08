import re

def parse_rpm(output_file):
    packages = []
    with open(output_file, "r") as file:
        for line in file:
            match = re.match(r'^(.*?)-(\d[\w\.\~]*)(?:-[\w\.]+)?\.\w+$', line.strip())
            if match:
                package_name, package_version = match.groups()
                packages.append((package_name, package_version))
    return packages
