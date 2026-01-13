import subprocess
from datetime import datetime
import json

OUTPUT_FILE = "benchmarks/cpu_raw_output.txt"

def run_benchmark():
    command = [
        "sysbench", "cpu",
        "--threads=4",
        "--time=10",
        "run"
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write(result.stdout)

    print("Benchmark completed")

if __name__ == "__main__":
    run_benchmark()
