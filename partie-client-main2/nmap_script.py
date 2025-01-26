import subprocess
import re

def scan_ports(ip):
    result = subprocess.run(['nmap', '-p-', ip], capture_output=True, text=True)
    if result.returncode == 0:
        ports = re.findall(r'(\d+/tcp)\s+(\S+)', result.stdout)
        return "\n".join([f"{port[0]}  {port[1]}" for port in ports])
    return None

def scan_os(ip):
    result = subprocess.run(['nmap', '-O', ip], capture_output=True, text=True)
    if result.returncode == 0:
        os_info = re.search(r'Running: (.*)\n', result.stdout)
        if os_info:
            return f"Running: {os_info.group(1)}"
    return None

def scan_services(ip):
    result = subprocess.run(['nmap', '-sV', ip], capture_output=True, text=True)
    if result.returncode == 0:
        services = re.findall(r'(\d+/tcp)\s+open\s+(\S+)\s+(\S+)', result.stdout)
        return "\n".join([f"{service[0]}  {service[1]}  {service[2]}" for service in services])
    return None

