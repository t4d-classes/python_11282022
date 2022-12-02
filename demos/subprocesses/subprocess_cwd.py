import subprocess
import pathlib
import os

# result = subprocess.run(["python", "-m", "demos"])

# working_folder = pathlib.Path(os.getcwd(), "..", "..")
working_folder = pathlib.Path(os.path.dirname(__file__), "..", "..")

result = subprocess.run(["python", "-m", "demos"], cwd=working_folder)

if result.returncode != 0:
    print("process exit unsuccessfully")
else:
    print("process exited successfully")
