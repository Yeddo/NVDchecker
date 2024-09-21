import os                           # Directory processing
import xml.etree.ElementTree as ET  # For SWID parser/XML.
from tqdm import tqdm               # Import tqdm for progress bar.

# Function to parse xml SWID Tags generated from yocto build.
def sbom_parser(dir_path):
    # Create an empty list to store the software identity details
    software_identity_list = []

    # Counters to keep track of # of files processed and errors encountered.
    count = 0  # Counter for number of files processed.
    errCount = 0  # Counter for number of error files processed.

    files = os.listdir(dir_path)  # List all files in the directory
    total_files = len(files)  # Get the total number of files

    # Iterate over files in the provided directory with tqdm progress bar
    for filename in tqdm(files, desc="Processing SWID tags", unit="file", dynamic_ncols=True):
        file = os.path.join(dir_path, filename)  # Join filename with path.
        if os.path.isfile(file):  # Checking if the file is in fact a file.
            if filename != 'cyclonedx.xml':  # Skip the cyclonedx.xml file.
                try:
                    tree = ET.parse(file)  # Parse the current file xml tree.
                    root = tree.getroot()  # Get root node/Element of tree.

                    # Check if the root tag is SoftwareIdentity, skip otherwise.
                    if root.tag != '{http://standards.iso.org/iso/19770/-2/2015/schema.xsd}SoftwareIdentity':
                        errCount += 1
                        count += 1
                        continue

                    # Extract the name and version attributes from the SoftwareIdentity tag.
                    name = root.attrib.get('name')
                    version = root.attrib.get('version')

                    if name and version:
                        # Append the software identity information to the list.
                        software_identity_list.append({'name': name, 'version': version})
                    
                    # Counter for counting number of files processed.
                    count += 1
                except ET.ParseError:
                    # Handle XML parsing errors
                    errCount += 1
            else:
                # Increment error count for cyclonedx.xml being skipped.
                errCount += 1
                count += 1

    # Print processing information to terminal.
    print(f'''
        Total files processed: {str(count)}
        Total files with errors: {str(errCount)}
        Total completed: {str(count - errCount)}\n
    ''')

    # Return the list of parsed software identities instead of writing to a file.
    return software_identity_list
