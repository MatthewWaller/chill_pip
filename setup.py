from setuptools import setup, find_packages

setup(
    name="chill_pip",
    version="0.1.0",
    author="Matthew Waller",
    author_email="admin@sapientai.io",
    description="A Dash application with obfuscated functionality",
    packages=find_packages(),
    include_package_data=True,
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
