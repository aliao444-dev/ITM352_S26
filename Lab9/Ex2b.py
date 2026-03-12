import os

filename = "my_custom_spreadsheet.csv"

# Check if the file exists and if the user has read permissions
if os.path.exists(filename) and os.access(filename, os.R_OK):
    # Retrieve file stats
    file_stats = os.stat(filename)
    
    print(f"File Information for {filename}:")
    print(f"Size: {file_stats.st_size} bytes")
    # oct() is used to show standard Unix-style permissions
    print(f"Permissions: {oct(file_stats.st_mode)}")
    
    # Open the file since we verified it exists and is readable
    with open(filename, 'r') as f:
        print("File successfully opened.")
else:
    print("Error: File does not exist or is not readable.")