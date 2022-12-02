import subprocess
import sys

# result = subprocess.run(
#     ["python", "echo.py", "hope and peace"], capture_output=True)
# result = subprocess.run(
#     ["python", "echo.py"], capture_output=True)
result = subprocess.run(
    ["python", "echo.py", "hope and peace"], capture_output=True, text=True)

if result.returncode != 0:
    print("process exit unsuccessfully")

    print(result.stderr)
    # print(result.stderr.decode('UTF-8'))

else:
    print("process exited successfully")

    print(result.stdout)
    # print(result.stdout.decode('UTF-8'))
