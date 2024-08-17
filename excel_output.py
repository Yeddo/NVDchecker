import openpyxl
from openpyxl.utils import get_column_letter

def save_to_excel(cve_results, output_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "CVE Report"
    headers = ["Package Name", "Package Version", "CVE ID", "CVSS Score", "Published Date", "Description"]
    ws.append(headers)

#    for i, header in enumerate(headers, 1):
#            ws.column_dimensions[get_column_letter(i)].width = 20

    for result in cve_results:
        ws.append(result)

    wb.save(output_file)
