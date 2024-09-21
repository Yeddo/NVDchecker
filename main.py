from parsers import dpkg_parser, rpm_parser, opkg_parser, sbom_parser
from nvd_lookup import nvd_search
from excel_output import save_to_excel
from utils import parse_args
from utils import delay_print

print (r'''
    .----.   @   @
   / .-"-.`.  \v/
   | | '\ \ \_/ )
 ,-\ `-.' /.'  /
'---`----'----'
''')
delay_print(r"Snail CVE Lookup Tool ... ¯\_(ツ)_/¯")
print ('\n')

def main():
    args = parse_args()

    if args.sbom:
        packages = sbom_parser.parse_sbom(args.input_file)
    
    if args.package_manager == "dpkg":
        packages = dpkg_parser.parse_dpkg(args.input_file)
    elif args.package_manager == "rpm":
        packages = rpm_parser.parse_rpm(args.input_file)
    elif args.package_manager == "opkg":
        packages = opkg_parser.parse_opkg(args.input_file)
    
    cve_results = nvd_search(packages, args.api_key)
    save_to_excel(cve_results, args.output_file)

if __name__ == "__main__":
    main()
