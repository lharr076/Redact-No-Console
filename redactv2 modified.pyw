import os
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def redact_specific_ip_addresses(log_content, ip1, ip2):
    ip_pattern = rf'\b(?:{re.escape(ip1)}|{re.escape(ip2)})\b'
    redacted_content = re.sub(ip_pattern, 'REDACTED', log_content)
    return redacted_content

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def redact_snort_log():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    base_directory = os.path.abspath('C:/Users/User/Documents/snort logs')
    while True:
        input_file = os.path.abspath(filedialog.askopenfilename(title="Select the log file to redact"))
        if os.path.commonpath([base_directory]) == os.path.commonpath([base_directory, input_file]):
            break
        messagebox.showinfo("Error", "The file does not exist or access denied. Please select a valid file.")

    ip1 = simpledialog.askstring("Input", "Enter the first IP address to redact:")
    ip2 = simpledialog.askstring("Input", "Enter the second IP address to redact:")
    if not ip1 or not ip2:
        messagebox.showinfo("Error", "IP address input cancelled.")
        return

    output_file = filedialog.asksaveasfilename(title="Save redacted log as", defaultextension=".txt")
    if not output_file:
        messagebox.showinfo("Error", "File save cancelled.")
        return

    try:
        log_content = read_file(input_file)
        redacted_content = redact_specific_ip_addresses(log_content, ip1, ip2)
        write_file(output_file, redacted_content)
        messagebox.showinfo("Success", f"Redacted log saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Call the function to start the process
redact_snort_log()
