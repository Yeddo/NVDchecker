import openpyxl

def create_excel_output(output_file, results):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Vulnerability Report"
    
    headers = ["Package Name", "Package Version", "CVE ID", "CVSS Score", "Published Date", "Description"]
    ws.append(headers)
    
    for result in results:
        ws.append(result)
    
    wb.save(output_file)
