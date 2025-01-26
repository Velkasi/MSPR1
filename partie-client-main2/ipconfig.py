import subprocess
import re
import time

result = subprocess.run(["ipconfig"], capture_output=True, text=True)

ipconfig_output = result.stdout

ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})"
match = re.search(ip_pattern, ipconfig_output)

if match:
	ip_parts = match.group(1).split(".")
	ip_parts[-1] = "0/24"
	modified_ip = ".".join(ip_parts)

	print(f"Adresse IP modifiée : {modified_ip}")

	nmap_result = subprocess.run(["nmap", "-PI", "-O", "sV", "-F", modified_ip], capture_output=True, text=True)

	print(nmap_result.stdout)
	time.sleep(10)
else:
	print("Aucune adresse IP trouvée.")


print(ipconfig_output)