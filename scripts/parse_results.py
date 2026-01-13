import re
import json
from datetime import datetime

INPUT_FILE = "benchmarks/cpu_raw_output.txt"
OUTPUT_FILE = "benchmarks/cpu_results.json"

def parse_results():
    with open(INPUT_FILE) as f:
        data = f.read()

    events = re.search(r"events per second:\s+([\d\.]+)", data)
    total_time = re.search(r"total time:\s+([\d\.]+)s", data)

    results = {
        "timestamp": datetime.utcnow().isoformat(),
        "events_per_second": float(events.group(1)) if events else None,
        "total_time_sec": float(total_time.group(1)) if total_time else None,
        "threads": 4,
        "tool": "sysbench"
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print("Results parsed")

if __name__ == "__main__":
    parse_results()
