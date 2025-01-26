import subprocess

def ping_8_8_8_8():
    ping_result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True)
    if "Moyenne =" in ping_result.stdout:
        latency = ping_result.stdout.split('Moyenne = ')[-1].split('\n')[0].strip()
        return latency
    return None

