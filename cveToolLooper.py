# ***********************************************************************
# AUTHOR = Jason Bisnette
# COPYRIGHT = 
# LICENSE = 
# VERSION = 1.0
# EMAIL = bisnettj@gdls.com
# DESCRIPTION = This script runs the cve-bin-tool.py on a folder of files
# USAGE = .\<tool>.py
# FILENAME = <tool>.py
# ***********************************************************************
# import required module
import os
import subprocess
import sys

# Error handling ...
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('\nError: This command requires exactly 1 argument\n')
    print('Example: python <tool>.py Dir\n')
    exit()

#if os.path.exists(sys.argv[1]) == False:
#    print('ERROR: The path supplied does not exist: ' +sys.argv[1]'\n')
    exit()

# Assign directories for input and output location.
directory = str(sys.argv[1])
# assign directory
#directory = (r"C:\Users\GDLSO06\Desktop\swids\swids\pit-edge-hypervisor-deploy-image")

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        subprocess.call('cve-bin-tool --sbom swid --sbom-file f --nvd-api-key 9e0a566b-c66d-487b-bc98-0b64773224ff -l debug -o c:\\Users\GDLSO06\\Desktop\\report.txt', shell=True)
