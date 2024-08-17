# Run:
opkg list-installed > opkgList.txt

# Export off system.
winscp
scp
etc.

# Run:
cat opkgList.txt | sed 's/[+].*$//' | sed 's/\-r.*//' | sed 's/\~r.*//' | sed '/-/!d' > newpackageTest.txt

or

nvd-cve-tool_v3.py <paramteres>

# To run on sbom folder of files:
python .\nvd-cve-tool_v2.py -s sbom -f C:\Users\GDLSO06\Desktop\PIT_EDGE\swid\pit-edge-hypervisor-deploy-image -o C:\Users\GDLSO06\Desktop\PIT_EDGE\cve\output.txt -k 9e0a566b-c66d-487b-bc98-0b64773224ff

# To run on the file with the output of 'opkg list-installed' command:
python .\nvd-cve-tool_v2.py -s sbom -i C:\Users\GDLSO06\Desktop\PIT_EDGE\cve\opkgList.txt -o C:\Users\GDLSO06\Desktop\PIT_EDGE\cve\output.txt -k 9e0a566b-c66d-487b-bc98-0b64773224ff

Both of the above options will create an output file (outputfile.txt) that contains the "fixed" package names after running through the parser. It will also create an excel document named "output.xlsx" in that location with the results from the NVD cve checks against the package names.

# RPM
rpm -qa --queryformat "%{NAME} - %{VERSION}\n"

