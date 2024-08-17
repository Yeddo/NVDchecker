import re

def parse_rpm(output_file):
    packages = []
    with open(output_file, 'r') as file:
        for line in file:
            match = re.match(r"(.+?)\s*-\s*(.+)", line.strip())
            if match:
                packages.append((match.group(1), match.group(2)))
    return packages

def parse_dpkg(output_file):
    packages = []
    with open(output_file, 'r') as file:
        for line in file:
            package, version = line.strip().split()
            packages.append((package, version))
    return packages

def parse_opkg(output_file):
    packages = []
    with open(output_file, 'r') as file:
        for line in file:
            match = re.match(r"(.+?)\s*-\s*(.+)", line.strip())
            if match:
                packages.append((match.group(1), match.group(2)))
    return packages
