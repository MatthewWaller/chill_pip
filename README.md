# Chill Pip - Obfuscated Package

A simple Dash application with obfuscated functionality.

## Installation

### Option 1: Automatic installation (recommended)

```bash
pip install git+https://github.com/MatthewWaller/chill_pip/
```

This will automatically select and install the appropriate wheel for your Python version and operating system.

### Option 2: Direct wheel installation

Download and install a specific wheel for your platform. Replace the filename with one that matches your OS and Python version:

```bash
# Direct download and install (example for macOS with Python 3.8)
pip install https://raw.githubusercontent.com/MatthewWaller/chill_pip/main/dist/wheels/chill_pip-0.1.0-cp38-cp38-macosx_11_0_universal2.whl
```

## Usage

After installation, you can run the application with:

```
chill-pip
```

Or you can use it in your own Python code:

```python
from chill_pip.app import app

app.run_server(debug=True)
```
