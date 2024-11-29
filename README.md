# MoodFetch: System Performance Mood Tracker

## Overview

MoodFetch is an innovative utility designed to provide an intuitive and visually engaging assessment of system performance. By analyzing various system metrics, MoodFetch translates complex technical data into an easily understandable "mood" representation.

## Features

- Real-time system performance analysis
- Colorful, emoji-enhanced mood reporting
- Detailed or minimal output modes
- Cross-distribution compatibility

## Prerequisites

Ensure you have the following requirements before installation:

- Python 3.8+
- pip (Python package manager)
- Basic system monitoring utilities

## Installation

### Arch Linux (Pacman)

```bash

# Manual installation
git clone https://github.com/sudo-seraphina/moodfetch.git
cd moodfetch
sudo python -m pip install .
```

### Debian/Ubuntu

```bash
# Update package lists
sudo apt update

# Install dependencies
sudo apt install python3-pip python3-dev build-essential

# Clone and install
git clone https://github.com/sudo-seraphina/moodfetch.git
cd moodfetch
sudo python3 -m pip install .
```

### Fedora

```bash
# Install dependencies
sudo dnf install python3-pip python3-devel

# Clone and install
git clone https://github.com/sudo-seraphina/moodfetch.git
cd moodfetch
sudo python3 -m pip install .
```

## Usage

### Basic Usage

```bash
# Display system mood
moodfetch

# Verbose mode (detailed metrics)
moodfetch -v

# Minimal mode (just mood and emoji)
moodfetch -m
```

### Command-Line Options

- `-v` or `--verbose`: Display comprehensive system metrics
- `-m` or `--minimal`: Show only mood and emoji

## Example Outputs

### Standard Output
```
==================================================
||       SYSTEM MOOD DIAGNOSTIC        ||
==================================================

🟢 Status: EXCELLENT 😄

System Visualization:
[ASCII Art Representation]

==================================================
|| Analyzed at: 2024-03-15 14:23:45 ||
==================================================
```

### Verbose Output
```
==================================================
||       SYSTEM MOOD DIAGNOSTIC        ||
==================================================

🟢 Status: EXCELLENT 😄

System Visualization:
[ASCII Art Representation]

🔍 Detailed System Metrics:
✅ CPU Usage: 35%
✅ Memory Utilization: 42%
⚠️ Disk Space: 65%
🚨 Network Latency: 95ms

==================================================
|| Analyzed at: 2024-03-15 14:23:45 ||
==================================================
```

## Troubleshooting

1. **Permission Issues**: Ensure you have the necessary system monitoring permissions.
2. **Python Version**: Verify you're using Python 3.8 or later.
3. **Dependency Problems**: Use `pip install -r requirements.txt` to resolve missing dependencies.

## Contributing

Contributions are welcome! 

## Contact

For issues, suggestions, or contributions, please open an issue on our GitHub repository.

## License
This project is licensed under the MIT License 

## Acknowledgements
The psutil library for providing system metrics.
Inspiration from various system monitoring tools.
