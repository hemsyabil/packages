import os
import subprocess

# List of packages to install in order
packages = [
    "Jinja2-3.1.4.tar.gz",
    "MarkupSafe-3.0.2.tar.gz",
    "Werkzeug-3.1.3.tar.gz",
    "blinker-1.9.0.tar.gz",
    "click-8.1.7.tar.gz",
    "flask-3.1.0.tar.gz",
    "itsdangerous-2.2.0.tar.gz"
]

# Path to the directory containing the .tar.gz files
packages_dir = "packages"

# Iterate through the list of packages and install each one
for package in packages:
    package_path = os.path.join(packages_dir, package)
    
    # Check if the package file exists
    if not os.path.exists(package_path):
        print(f"Error: {package} not found in {packages_dir}. Skipping.")
        continue
    
    print(f"Installing {package}...")
    try:
        subprocess.check_call([
            "pip", "install", package_path,
            "--no-index", "--no-deps", "--no-build-isolation"
        ])
        print(f"{package} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}. Error: {e}")

print("Installation process completed.")

