# CVE Scanner

## Overview
The CVE Scanner is a Python tool designed to parse package manager listings (from `rpm`, `dpkg`, and `opkg`), perform a lookup in the National Vulnerability Database (NVD) for associated Common Vulnerabilities and Exposures (CVEs), and generate a report in excel.

It has been updated to use the 2.0 API.

## Features
- **Package Manager Support:** Handles output from `dpkg`, `rpm`, and `opkg`.
- **NVD Lookup:** Queries the NVD API to retrieve CVEs associated with each package and version.
- **Excel Report:** Outputs the results into an Excel spreadsheet for easy analysis.
- **Modular Design:** Easily extendable and maintainable codebase.

## Prerequisites
- Python 3.x
- Install required Python packages by running:
```bash
pip3 install -r requirements.txt
```


## Usage

### Command-Line Arguments
- `--package-manager`: Specify the package manager (`dpkg`, `rpm`, or `opkg`).
- `--input-file`: File containing the package listing from the package manager.
- `--output-file`: Output Excel file name (default: `cve_report.xlsx`).
- `--api-key`: NVD API key (optional but recommended to avoid rate limits).
- `--sbom`: SBOM parser (SWID tags from SWID yocto receipe specifically) May not work with other SBOM formats.

### Example Command
```bash
python main.py --package-manager dpkg --input-file dpkgList.txt --output-file cve_report.xlsx --api-key your-nvd-api-key
```

## Input File Generation from Host
- For `dpkg`: Generate the package list using `dpkg-query -W -f='${Package} - ${Version}\n' > dpkgList.txt`
- For `rpm`: Generate the package list using `rpm -qa --queryformat "%{NAME} - %{VERSION}\n" > rpmList.txt`
- For `opkg`: Generate the package list using `opkg list-installed > opkgList.txt`

## Output
- An Excel file containing a list of packages with associated CVEs, CVSS scores, published dates, and descriptions.

## Project Structure
```
cve_scanner/
│
├── parsers/
│   ├── dpkg_parser.py
│   ├── rpm_parser.py
│   └── opkg_parser.py
│
├── nvd_lookup.py
├── excel_output.py
├── main.py
├── utils.py
└── README.md
```

## License
This project is licensed under the MIT License.

## NOTES
https://nvd.nist.gov/developers/vulnerabilities

https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:*:*:*:*:*:*:*

CPE Format (v2.3):
```bash
cpe:2.3:<part>:<vendor>:<product>:<version>:<update>:<edition>:<language>:<sw_edition>:<target_sw>:<target_hw>:<other>
```
Breakdown:

    <part>: This identifies the type of product:
        a for applications (software)
        o for operating systems
        h for hardware
    <vendor>: The vendor or manufacturer of the product.
    <product>: The name of the product.
    <version>: The version number of the product.
    <update>: The update level of the product.
    <edition>: The edition of the product.
    <language>: The language of the product.
    <sw_edition>: The software edition (e.g., Professional, Enterprise).
    <target_sw>: The target software environment (e.g., Android, iOS).
    <target_hw>: The target hardware environment (e.g., ARM, x86).
    <other>: Other variations of the product.
  
