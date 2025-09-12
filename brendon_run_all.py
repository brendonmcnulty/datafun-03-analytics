"""
Main processing script to run all fetch + process scripts in sequence.
"""

import subprocess
import sys
import pathlib

# Scripts to run in order
SCRIPTS_TO_RUN = [
    "brendon_get_excel.py",
    "brendon_process_excel.py",
    "brendon_get_text.py",
    "brendon_process_text.py",
    "brendon_get_csv.py",
    "brendon_process_csv.py",
    "brendon_get_json.py",
    "brendon_process_json.py",
]

def run_script(script_name):
    """Run a script and print status."""
    print(f"⏳ Running: {script_name}")
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ Success: {script_name}")
            if result.stdout.strip():
                print(result.stdout.strip())
        else:
            print(f"❌ Failed: {script_name}")
            if result.stderr.strip():
                print(result.stderr.strip())
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")

def main():
    repo_dir = pathlib.Path(__file__).resolve().parent
    for script in SCRIPTS_TO_RUN:
        script_path = repo_dir / script
        if script_path.exists():
            run_script(str(script_path))
        else:
            print(f"❌ Not found: {script}")

if __name__ == "__main__":
    main()
