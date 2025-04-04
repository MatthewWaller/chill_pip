from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
        'chill_pip': [
            'pytransform/*.py',
            'pytransform/*.so',
            'pytransform/*.dll',
            'pytransform/*.dylib',
            'pytransform/platforms/*/*/*',
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