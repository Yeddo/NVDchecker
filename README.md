# CVE Scanner

## Overview
The CVE Scanner is a Python tool designed to parse package manager listings (from `rpm`, `dpkg`, and `opkg`), perform a lookup in the National Vulnerability Database (NVD) for associated Common Vulnerabilities and Exposures (CVEs), and generate a well-formatted Excel report.

## Features
- **Package Manager Support:** Handles output from `dpkg`, `rpm`, and `opkg`.
- **NVD Lookup:** Queries the NVD API to retrieve CVEs associated with each package and version.
- **Excel Report:** Outputs the results into an Excel spreadsheet for easy analysis.
- **Modular Design:** Easily extendable and maintainable codebase.

## Prerequisites
- Python 3.x
- Install required Python packages by running:

```bash
pip install requests openpyxl
```

## Usage

### Command-Line Arguments
- `--package-manager`: Specify the package manager (`dpkg`, `rpm`, or `opkg`).
- `--input-file`: File containing the package listing from the package manager.
- `--output-file`: Output Excel file name (default: `cve_report.xlsx`).
- `--api-key`: NVD API key (optional but recommended to avoid rate limits).

### Example Command
```bash
python main.py --package-manager dpkg --input-file dpkgList.txt --output-file cve_report.xlsx --api-key your-nvd-api-key
```

## Input Files
- For `dpkg`: Generate the package list using `dpkg-query -W -f='${Package} ${Version}
' > dpkgList.txt`.
- For `rpm`: Generate the package list using `rpm -qa --queryformat "%{NAME} - %{VERSION}
" > rpmList.txt`.
- For `opkg`: Generate the package list using `opkg list-installed > opkgList.txt`.

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
