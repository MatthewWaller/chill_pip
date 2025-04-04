from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Ensure we include all necessary PyArmor files
def get_pytransform_files():
    pytransform_files = []
    for root, dirs, files in os.walk("chill_pip/pytransform"):
        for file in files:
            # Create relative path from chill_pip directory
            rel_path = os.path.join(root, file)
            if rel_path.startswith("chill_pip/"):
                rel_path = rel_path[len("chill_pip/"):]
            pytransform_files.append(rel_path)
    return pytransform_files

setup(
    name="chill_pip",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Dash application with secret functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chill_pip",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'chill_pip': get_pytransform_files() + [
            'pytransform/__init__.py',
            'pytransform/pytransform.py',
            'pytransform/_pytransform.dylib',
            'pytransform/_pytransform.dll',
            'pytransform/_pytransform.so',
            'pytransform/_pytransform_arm64.dylib',
            'pytransform/platforms/darwin/x86_64/_pytransform.dylib',
            'pytransform/platforms/darwin/arm64/_pytransform.dylib',
            'pytransform/platforms/windows/x86_64/_pytransform.dll',
            'pytransform/platforms/linux/x86_64/_pytransform.so',
            # Include license file
            'pytransform/license.lic',
            # Make sure all platform binaries are included
            'pytransform/platforms/**/*',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "dash>=2.0.0",
        "dash-bootstrap-components>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "chill-pip=chill_pip.run:main",
        ],
    },
) 