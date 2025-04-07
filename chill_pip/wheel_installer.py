import os
import sys
import platform
import subprocess

def find_and_install_wheel():
    """Find and install the appropriate wheel for the current system."""
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
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Try different possible locations for the wheels directory
    possible_locations = [
        wheels_dir,
        os.path.join(repo_root, 'dist', 'wheels'),
        os.path.join(os.path.dirname(repo_root), 'dist', 'wheels'),
    ]
    
    wheels = []
    for location in possible_locations:
        if os.path.exists(location):
            wheels = os.listdir(location)
            wheels_dir = location
            break
    
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
        return True
    else:
        print("No matching wheel found for your system. Available wheels:")
        for wheel in wheels:
            print(f"  - {wheel}")
        print(f"Python: {python_version}, OS: {system} ({os_name}), Architecture: {arch}")
        return False
