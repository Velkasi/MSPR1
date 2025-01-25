import json

def save_scan_results(scan_data, filename="scan_results.json"):
    with open(filename, 'a') as f:
        json.dump(scan_data, f, ensure_ascii=False, indent=4)
        f.write('\n\n')  # Add a blank line between each scan result
