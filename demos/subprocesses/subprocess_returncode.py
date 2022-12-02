import subprocess

# result = subprocess.run(["python", "echo.py", "some message"])
result = subprocess.run(["python", "echo.py"])

if result.returncode != 0:
    print("process exited unsuccessfully")
else:
    print("process exited successfully")
