import subprocess
import os

env_vars = {
    "PATH": os.environ["PATH"],
    "ENVIRONMENT": "Development"
}

subprocess.run(["python", "display_env_vars.py"], env=env_vars)
