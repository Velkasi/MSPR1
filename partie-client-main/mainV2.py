import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import subprocess
from datetime import datetime
import socket
import re

# Function to start the scan

def start_scan():
    # Record current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Get hostname
    hostname = socket.gethostname()
    
    # Ping 8.8.8.8
    ping_result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True)
    if "Moyenne =" in ping_result.stdout:
        latency = ping_result.stdout.split('Moyenne = ')[-1].split('\n')[0].strip()
        # Save successful ping result to JSON
        ping_data = {
            "datetime": current_time,
            "hostname": hostname,
            "ping_8.8.8.8": latency
        }
        with open('scan_results.json', 'a') as f:
            json.dump(ping_data, f, ensure_ascii=False, indent=4)
            f.write('\n')
        print("Ping réussi, données sauvegardées.")
    else:
        messagebox.showwarning("Ping Échoué", "Le ping vers 8.8.8.8 a échoué. Aucun résultat sauvegardé.")
        return  # Stop further scans if ping fails

    # Scan ports/IP
    ip = "localhost"  # Replace with the desired IP address if needed
    scan_results = {
        "datetime": current_time,
        "hostname": hostname,
        "ip": ip,
        "port_scan": None,
        "os_scan": None,
        "service_scan": None
    }

    # Port scan: We extract only the ports that are open and their services
    port_scan_result = subprocess.run(['nmap', '-p-', ip], capture_output=True, text=True)
    if port_scan_result.returncode == 0:
        # Filter out irrelevant information
        ports = re.findall(r'(\d+/tcp)\s+(\S+)', port_scan_result.stdout)
        port_scan_data = "\n".join([f"{port[0]}  {port[1]}" for port in ports])
        scan_results["port_scan"] = f"PORT    STATE    SERVICE\n{port_scan_data}"
    
    # OS scan: We extract only the OS information
    os_scan_result = subprocess.run(['nmap', '-O', ip], capture_output=True, text=True)
    if os_scan_result.returncode == 0:
        os_info = re.search(r'Running: (.*)\n', os_scan_result.stdout)
        if os_info:
            scan_results["os_scan"] = f"Running: {os_info.group(1)}"
    
    # Service scan: We extract only the services and versions
    service_scan_result = subprocess.run(['nmap', '-sV', ip], capture_output=True, text=True)
    if service_scan_result.returncode == 0:
        services = re.findall(r'(\d+/tcp)\s+open\s+(\S+)\s+(\S+)', service_scan_result.stdout)
        service_scan_data = "\n".join([f"{service[0]}  {service[1]}  {service[2]}" for service in services])
        scan_results["service_scan"] = f"PORT    STATE    SERVICE VERSION\n{service_scan_data}"
    
    # Save the complete scan result for this IP if any scan was successful
    if any(scan_results[key] is not None for key in ["port_scan", "os_scan", "service_scan"]):
        with open('scan_results.json', 'a') as f:
            json.dump(scan_results, f, ensure_ascii=False, indent=4)
            f.write('\n\n')  # Add a blank line between each scan result
        print(f"Résultats du scan pour {ip} sauvegardés dans scan_results.json.")
    
    # Update progress bar
    progress_var.set(100)
    progress_bar.update()
    
    # Show success message
    messagebox.showinfo("Success", "Scan effectué avec succès !")

# Setup Tkinter window
def setup_gui():
    global progress_var, progress_bar
    root = tk.Tk()
    root.title("Network Scanner")

    # Start button
    start_button = tk.Button(root, text="Démarrer", command=start_scan)
    start_button.pack(pady=20)

    # Progress bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.pack(pady=20, fill=tk.X, padx=20)

    root.mainloop()

# Run the GUI setup
setup_gui()




