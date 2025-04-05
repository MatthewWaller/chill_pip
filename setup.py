
from setuptools import setup, find_packages
import os

def get_pytransform_files():
    pytransform_files = []
    for root, dirs, files in os.walk("chill_pip/pytransform"):
        for file in files:
            rel_path = os.path.join(root, file)
            if rel_path.startswith("chill_pip/"):
                rel_path = rel_path[len("chill_pip/"):]
            pytransform_files.append(rel_path)
    return pytransform_files

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
)
