import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime_script import get_datetime
from ping_script import ping_8_8_8_8
from nmap_script import scan_ports, scan_os, scan_services
from scan_result_script import save_scan_results
import socket
import json

def start_scan():
    # Record current date and time
    current_time = get_datetime()
    
    # Get hostname
    hostname = socket.gethostname()
    
    # Ping 8.8.8.8
    ping_result = ping_8_8_8_8()

    # Scan ports/IP
    ip = "localhost"  # Replace with the desired IP address if needed
    scan_results = {
        "datetime": current_time,
        "hostname": hostname,
        "ip": ip,
        "ping": ping_result,
        "port_scan": scan_ports(ip),
        "os_scan": scan_os(ip),
        "service_scan": scan_services(ip)
    }

    # Save the complete scan result for this IP if any scan was successful
    if any(scan_results[key] is not None for key in ["port_scan", "os_scan", "service_scan"]):
        save_scan_results(scan_results)
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
