# Chill Pip

A Python package with obfuscated wheels.

## Installation

You can install the package in two ways:

### 1. Direct Installation (Recommended)

Simply run:
```bash
pip install git+https://github.com/yourusername/chill-pip-public.git
```

This will automatically detect your platform and Python version and install the appropriate wheel.

### 2. Manual Installation

If you prefer to install manually, you can download and install a specific wheel:

```bash
# For Windows (64-bit)
pip install https://raw.githubusercontent.com/yourusername/chill-pip-public/main/dist/wheels/chill_pip-0.1.0-cp38-cp38-win_amd64.whl

# For macOS (Intel)
pip install https://raw.githubusercontent.com/yourusername/chill-pip-public/main/dist/wheels/chill_pip-0.1.0-cp38-cp38-macosx_10_9_x86_64.whl

# For macOS (Apple Silicon)
pip install https://raw.githubusercontent.com/yourusername/chill-pip-public/main/dist/wheels/chill_pip-0.1.0-cp38-cp38-macosx_11_0_arm64.whl

# For Linux (x86_64)
pip install https://raw.githubusercontent.com/yourusername/chill-pip-public/main/dist/wheels/chill_pip-0.1.0-cp38-cp38-manylinux_2_17_x86_64.whl

# For Linux (ARM64)
pip install https://raw.githubusercontent.com/yourusername/chill-pip-public/main/dist/wheels/chill_pip-0.1.0-cp38-cp38-manylinux_2_17_aarch64.whl
```

Replace the version number and Python version in the URL with the appropriate one for your system.

## Available Wheels

The following wheels are available:

- Windows (64-bit): `chill_pip-0.1.0-cp38-cp38-win_amd64.whl`
- macOS (Intel): `chill_pip-0.1.0-cp38-cp38-macosx_10_9_x86_64.whl`
- macOS (Apple Silicon): `chill_pip-0.1.0-cp38-cp38-macosx_11_0_arm64.whl`
- Linux (x86_64): `chill_pip-0.1.0-cp38-cp38-manylinux_2_17_x86_64.whl`
- Linux (ARM64): `chill_pip-0.1.0-cp38-cp38-manylinux_2_17_aarch64.whl`

## Usage

After installation, you can run the application with:

```bash
chill-pip
```
