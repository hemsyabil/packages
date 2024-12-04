import os
import subprocess
import pkg_resources  # To check installed packages

# List of .whl files to install in order
packages = [
    # Flask supports
    "setuptools-75.6.0-py3-none-any.whl",
    "wheel-0.45.1-py3-none-any.whl",
    "flit_core-3.10.1-py3-none-any.whl",
    "jinja2-3.1.4-py3-none-any.whl",
    "MarkupSafe-3.0.2-cp39-cp39-win_amd64.whl",
    "werkzeug-3.1.3-py3-none-any.whl",
    "blinker-1.9.0-py3-none-any.whl",
    "click-8.1.7-py3-none-any.whl",
    "flask-3.1.0-py3-none-any.whl",
    "itsdangerous-2.2.0-py3-none-any.whl",
    "importlib_metadata-8.5.0-py3-none-any.whl",
    "colorama-0.4.6-py2.py3-none-any.whl",

    # Openpyxl supports
    "et_xmlfile-2.0.0-py3-none-any.whl",
    "openpyxl-3.1.5-py2.py3-none-any.whl",
    "lxml-5.3.0-cp39-cp39-win_amd64.whl",

    # Requests support
    "charset_normalizer-3.4.0-cp39-cp39-win_amd64.whl",
    "requests-2.32.3-py3-none-any.whl",
    "urllib3-2.2.3-py3-none-any.whl",

    # Argparse support
    "argparse-1.4.0-py2.py3-none-any.whl",

    # PUDB supports
    "jedi-0.19.2-py2.py3-none-any.whl",
    "packaging-24.2-py3-none-any.whl",
    "parso-0.8.4-py2.py3-none-any.whl",
    "pudb-2024.1.3-py3-none-any.whl",
    "pygments-2.18.0-py3-none-any.whl",
    "typing_extensions-4.12.2-py3-none-any.whl",
    "urwid-2.6.16-py3-none-any.whl",
    "urwid_readline-0.15.1.tar.gz",
    "wcwidth-0.2.13-py2.py3-none-any.whl",

    # Flake8 supports
    "flake8-7.1.1-py2.py3-none-any.whl",
    "mccabe-0.7.0-py2.py3-none-any.whl",
    "pycodestyle-2.12.1-py2.py3-none-any.whl",
    "pyflakes-3.2.0-py2.py3-none-any.whl",

    # Pandas supports
    "meson_python-0.17.1-py3-none-any.whl",
    "tomli-2.2.1-py3-none-any.whl",
    "numpy-2.1.3.tar.gz",
    "python_dateutil-2.9.0.post0-py2.py3-none-any.whl",
    "pytz-2024.2-py2.py3-none-any.whl",
    "tzdata-2024.2-py2.py3-none-any.whl",
    "six-1.16.0-py2.py3-none-any.whl",
    "pandas-2.2.3-cp39-cp39-win_amd64.whl"
]

# Path to the directory containing the .whl files
packages_dir = "packages"

# Iterate through the list of packages and install each one if not already installed
for package_file in packages:
    # Extract package name and version from the file name
    package_name = package_file.split("-")[0]
    package_version = package_file.split("-")[1]

    try:
        # Check if the package is already installed
        installed_version = pkg_resources.get_distribution(package_name).version
        if installed_version == package_version:
            print(f"{package_name} {package_version} is already installed. Skipping.")
            continue
        else:
            print(f"{package_name} is installed with version {installed_version}, but {package_version} is required. Installing...")
    except pkg_resources.DistributionNotFound:
        print(f"{package_name} is not installed. Installing...")

    # Construct the full path to the .whl file
    package_path = os.path.join(packages_dir, package_file)

    # Check if the .whl file exists
    if not os.path.exists(package_path):
        print(f"Error: {package_file} not found in {packages_dir}. Skipping.")
        continue

    # Install the .whl package
    try:
        subprocess.check_call([
            "pip", "install", package_path,
            "--no-index", "--no-deps", "--no-build-isolation"
        ])
        print(f"{package_name} {package_version} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name} {package_version}. Error: {e}")

print("Installation process completed.")
