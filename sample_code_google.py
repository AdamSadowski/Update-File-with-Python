# Define destination files
import_file = "allow_list.txt"
remove_file = "remove_list.txt"

# Open files for reading
with open(import_file, "r") as allow_list_file:
    ip_addr_lines = allow_list_file.readlines()

with open(remove_file, "r") as remove_list_file:
    remove_list_lines = remove_list_file.readlines()

# Convert file contents to lists
ip_addr = [line.strip() for line in ip_addr_lines]
remove_list = [line.strip() for line in remove_list_lines]

# Create a copy of the IP address list
filtered_ip_addr = ip_addr[:]

# Remove elements from the copy
for element in remove_list:
    if element in filtered_ip_addr:
        filtered_ip_addr.remove(element)

# Join the filtered IP addresses with spaces
filtered_ip_addr_str = " ".join(filtered_ip_addr)

# Write the filtered IP address list to the file
with open(import_file, "w") as allow_list_file:
    allow_list_file.write(filtered_ip_addr_str)