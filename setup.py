
from setuptools import setup, find_packages, Command
from setuptools.command.install import install
import os
import platform
import shutil
import sys

def get_pytransform_files():
    pytransform_files = []
    for root, dirs, files in os.walk("chill_pip/pytransform"):
        for file in files:
            rel_path = os.path.join(root, file)
            if rel_path.startswith("chill_pip/"):
                rel_path = rel_path[len("chill_pip/"):]
            pytransform_files.append(rel_path)
    return pytransform_files

# Special hook for ARM Macs
class CustomInstall(install):
    def run(self):
        # First run the standard install
        install.run(self)
        
        # Then do the ARM-specific setup
        if platform.system() == "Darwin" and platform.machine() == "arm64":
            print("Installing on ARM64 Mac - setting up ARM-compatible binary...")
            # Find the installed package
            if self.install_lib:
                pkg_dir = os.path.join(self.install_lib, "chill_pip", "pytransform")
            else:
                pkg_dir = os.path.join(sys.prefix, "lib", "python" + sys.version[:3], 
                                     "site-packages", "chill_pip", "pytransform")
            
            if os.path.exists(pkg_dir):
                # Find the ARM binary
                arm_paths = [
                    os.path.join(pkg_dir, "_pytransform_arm64.dylib"),
                    os.path.join(pkg_dir, "platforms", "darwin", "aarch64", "_pytransform.dylib")
                ]
                
                for arm_path in arm_paths:
                    if os.path.exists(arm_path):
                        dest_path = os.path.join(pkg_dir, "_pytransform.dylib")
                        print(f"Pre-copying ARM64 binary from {arm_path} to {dest_path}")
                        # Backup existing if needed
                        if os.path.exists(dest_path):
                            backup = os.path.join(pkg_dir, "_pytransform_x86.dylib")
                            if not os.path.exists(backup):
                                shutil.copy2(dest_path, backup)
                        # Copy ARM binary to main location
                        shutil.copy2(arm_path, dest_path)
                        print("Successfully prepared ARM64 binary")
                        break

setup(
    name="chill_pip",
    version="0.1.0",
    author="Matthew Waller",
    author_email="admin@sapientai.io",
    description="A simple Dash application with obfuscated functionality",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'chill_pip': get_pytransform_files() + [
            'pytransform/__init__.py',
            'pytransform/pytransform.py',
            'pytransform/_pytransform.dll',
            'pytransform/_pytransform.so',
            'pytransform/_pytransform.dylib',
            'pytransform/_pytransform_arm64.dylib',
            'pytransform/license.lic',
            'pytransform/platforms/darwin/x86_64/_pytransform.dylib',
            'pytransform/platforms/darwin/aarch64/_pytransform.dylib',
            'pytransform/platforms/windows/x86_64/_pytransform.dll',
            'pytransform/platforms/linux/x86_64/_pytransform.so',
        ],
    },
    install_requires=[
        "dash>=2.0.0",
        "dash-bootstrap-components>=1.0.0",
        "Flask>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "chill-pip=chill_pip.run:main",
        ],
    },
    cmdclass={
        'install': CustomInstall,
    },
)
