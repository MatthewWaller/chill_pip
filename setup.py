import os
import sys
import platform
import subprocess
import setuptools
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        system = platform.system().lower()
        machine = platform.machine().lower()
        
        # Map platform to wheel naming convention
        os_map = {
            'darwin': 'macosx',
            'linux': 'linux',
            'windows': 'win'
        }
        
        # Map machine architecture
        arch_map = {
            'x86_64': 'x86_64',
            'amd64': 'x86_64',
            'i386': 'i386',
            'i686': 'i386',
            'arm64': 'aarch64',
            'aarch64': 'aarch64'
        }
        
        os_name = os_map.get(system, system)
        arch = arch_map.get(machine, machine)
        
        # Handle macOS universal2 wheel
        if system == 'darwin':
            # Modern macOS uses universal2 wheels
            arch = 'universal2'
            # macOS version detection (simplified)
            mac_ver = '.'.join(platform.mac_ver()[0].split('.')[:2])
            os_name = f"macosx_{mac_ver.replace('.', '_')}"
        
        # Python ABI tag (simplified)
        cp_version = f"cp{sys.version_info.major}{sys.version_info.minor}"
        
        # Pattern to look for
        wheel_pattern = f"chill_pip-0.1.0-{cp_version}-{cp_version}"
        
        # Windows has a different naming convention
        if system == 'windows':
            # Check for different Windows wheel naming patterns
            possible_patterns = [
                f"{wheel_pattern}-win_{arch}.whl",
                f"{wheel_pattern}-win32.whl",
                f"{wheel_pattern}-win_amd64.whl"
            ]
        elif system == 'darwin':
            possible_patterns = [
                f"{wheel_pattern}-{os_name}_universal2.whl",
                f"{wheel_pattern}-{os_name}_{arch}.whl",
                f"{wheel_pattern}-macosx_10_9_universal2.whl",
                f"{wheel_pattern}-macosx_11_0_universal2.whl"
            ]
        else:  # Linux and others
            possible_patterns = [
                f"{wheel_pattern}-{os_name}_{arch}.whl",
                f"{wheel_pattern}-manylinux1_{arch}.whl",
                f"{wheel_pattern}-manylinux2010_{arch}.whl",
                f"{wheel_pattern}-manylinux2014_{arch}.whl"
            ]
        
        # Find available wheels
        wheels_dir = os.path.join('dist', 'wheels')
        if not os.path.exists(wheels_dir):
            print(f"Warning: Wheels directory not found at {wheels_dir}")
            wheels_dir = os.path.join(os.path.dirname(__file__), 'dist', 'wheels')
            
        wheels = os.listdir(wheels_dir) if os.path.exists(wheels_dir) else []
        
        # Try to find a matching wheel
        matching_wheel = None
        for pattern in possible_patterns:
            for wheel in wheels:
                if pattern in wheel:
                    matching_wheel = os.path.join(wheels_dir, wheel)
                    break
            if matching_wheel:
                break
        
        if matching_wheel:
            print(f"Installing matching wheel: {matching_wheel}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', matching_wheel])
        else:
            print("No matching wheel found for your system. Available wheels:")
            for wheel in wheels:
                print(f"  - {wheel}")
            print(f"Python: {python_version}, OS: {system} ({os_name}), Architecture: {arch}")
            raise Exception("Could not find a compatible wheel for your system")

setuptools.setup(
    name="chill_pip",
    version="0.1.0",
    author="Matthew Waller",
    author_email="author@example.com",
    description="A Dash application with obfuscated functionality",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MatthewWaller/chill_pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    cmdclass={
        'install': CustomInstall,
    },
    entry_points={
        'console_scripts': [
            'chill-pip=chill_pip.app:main',
        ],
    },
)
