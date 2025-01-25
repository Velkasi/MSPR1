import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import subprocess
import datetime

# Function to start the scan

def start_scan():
    # Record current date and time
    current_time = "2025-01-10 00:42:42.219327"
    
    # Ping 8.8.8.8
    ping_result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True)
    # Extract average ping time
    average_ping_time = "Moyenne = " + ping_result.stdout.split('Moyenne = ')[-1].split('\n')[0].strip()
    
    # Network and port scan using nmap
    nmap_result = subprocess.run(['nmap', '-sP', '127.0.0.1/24'], capture_output=True, text=True)
    port_scan_result = subprocess.run(['nmap', '-p-', 'localhost'], capture_output=True, text=True)
    
    # Print network and port scan results to terminal
    print("Network Scan Result:")
    print(nmap_result.stdout)
    print("Port Scan Result:")
    print(port_scan_result.stdout)
    
    # Save results to JSON file
    data = {
        'time': current_time,
        'ping': average_ping_time,
        'network_scan': nmap_result.stdout,
        'port_scan': port_scan_result.stdout
    }
    with open('scan_results.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
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