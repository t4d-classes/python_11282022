import os

print(os.environ.values())

for var_name, var_value in os.environ.items():
    print(f"{var_name}: {var_value}")
