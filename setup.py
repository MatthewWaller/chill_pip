import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

# Get the current directory
here = os.path.abspath(os.path.dirname(__file__))

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # First run the standard install
        install.run(self)
        
        # Then try to install the appropriate wheel
        try:
            from chill_pip.wheel_installer import find_and_install_wheel
            find_and_install_wheel()
        except Exception as e:
            print(f"Failed to install wheel: {e}")
            # Continue even if wheel installation fails
            # This allows the base package to install

setup(
    name="chill_pip",
    version="0.1.0",
    author="Matthew Waller",
    author_email="author@example.com",
    description="A simple Dash application with obfuscated functionality",
    long_description=open(os.path.join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MatthewWaller/chill_pip",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "dash>=2.0.0",
        "dash-bootstrap-components>=1.0.0",
        "Flask>=2.0.0",
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'chill-pip=chill_pip.app:main',
        ],
    },
    include_package_data=True,
)
