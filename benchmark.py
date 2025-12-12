#!/usr/bin/env python3
import subprocess
import time
import sys
import os

def run_benchmark(day, test_file="small_test.csv"):
    day_dir = f"day-{day}"
    if not os.path.exists(day_dir):
        print(f"Day {day} directory not found")
        return
    
    os.chdir(day_dir)
    results = {}
    
    # Python
    if os.path.exists("solution.py"):
        start = time.time()
        result = subprocess.run(["python3", "solution.py", test_file], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            results["Python"] = time.time() - start
    
    # Rust
    if os.path.exists("solution.rs"):
        subprocess.run(["rustc", "-O", "solution.rs"], capture_output=True)
        if os.path.exists("solution"):
            start = time.time()
            result = subprocess.run(["./solution", test_file], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                results["Rust"] = time.time() - start
            os.remove("solution")
    
    # JavaScript
    if os.path.exists("solution.js"):
        start = time.time()
        result = subprocess.run(["node", "solution.js", test_file], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            results["JavaScript"] = time.time() - start
    
    os.chdir("..")
    
    print(f"Day {day} Performance:")
    for lang, duration in sorted(results.items(), key=lambda x: x[1]):
        print(f"  {lang}: {duration:.3f}s")
    print()

if __name__ == "__main__":
    day = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    run_benchmark(day)