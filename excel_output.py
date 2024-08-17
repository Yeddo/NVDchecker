import openpyxl

def save_to_excel(cve_results, output_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "CVE Report"

    headers = ["Package Name", "Package Version", "CVE ID", "CVSS Score", "Published Date", "Description"]
    ws.append(headers)

    for result in cve_results:
        ws.append(result)

    wb.save(output_file)
