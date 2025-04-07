import os
import sys
import platform
import subprocess
from setuptools import setup
from setuptools.command.install import install
from pathlib import Path

def get_python_version():
    """Get the Python version as a string (e.g., '3.8')."""
    return f"{sys.version_info.major}.{sys.version_info.minor}"

def get_platform_tag():
    """Get the platform tag for wheel selection."""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == 'linux':
        if machine == 'x86_64':
            return 'manylinux_2_17_x86_64'
        elif machine == 'aarch64':
            return 'manylinux_2_17_aarch64'
    elif system == 'darwin':
        if machine == 'x86_64':
            return 'macosx_10_9_x86_64'
        elif machine == 'arm64':
            return 'macosx_11_0_arm64'
    elif system == 'windows':
        if machine == 'amd64' or machine == 'x86_64':
            return 'win_amd64'
        else:
            return 'win32'
    return None

def find_matching_wheel():
    """Find a wheel that matches the current platform and Python version."""
    py_version = get_python_version()
    platform_tag = get_platform_tag()
    
    if not platform_tag:
        print(f"Unsupported platform: {platform.system()} {platform.machine()}")
        return None
    
    # Look for wheels in the dist/wheels directory
    wheels_dir = Path(__file__).parent / 'dist' / 'wheels'
    if not wheels_dir.exists():
        print(f"Wheels directory not found: {wheels_dir}")
        return None
    
    # Try to find an exact match first
    for wheel_path in wheels_dir.glob(f"chill_pip-*-{py_version}-{py_version}*-{platform_tag}.whl"):
        return wheel_path
    
    # Try to find a compatible match
    for wheel_path in wheels_dir.glob(f"chill_pip-*-{py_version}-*.whl"):
        return wheel_path
    
    # Try to find any wheel for this Python version
    for wheel_path in wheels_dir.glob(f"chill_pip-*-{py_version}*.whl"):
        return wheel_path
    
    # Fall back to any wheel
    for wheel_path in wheels_dir.glob("chill_pip-*.whl"):
        return wheel_path
    
    return None

class CustomInstall(install):
    def run(self):
        wheel_path = find_matching_wheel()
        if wheel_path:
            print(f"Found matching wheel: {wheel_path.name}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", str(wheel_path)])
        else:
            print("\nNo matching wheel found for your platform.")
            print("Please download and install a specific wheel from the list in the README.")
            sys.exit(1)

setup(
    name="chill-pip",
    version="0.1.0",
    description="A Python package with obfuscated wheels",
    author="Your Name",
    author_email="your.email@example.com",
    cmdclass={'install': CustomInstall},
    python_requires='>=3.8',
    packages=[],  # No Python packages to include
    exclude_package_data={'': ['downloaded_wheels/*', 'dist/*']},  # Exclude wheel directories
    include_package_data=True,  # Include non-Python files
    package_data={
        '': ['dist/wheels/*.whl'],  # Include only the wheel files
    },
)
