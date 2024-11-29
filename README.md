# Moodfetch

**Moodfetch** is a lightweight and customizable system monitoring tool that provides a quick overview of system metrics, including CPU load, memory usage, disk usage, and uptime. It is designed for users who want to track their system's performance in a minimalist yet informative way, with a focus on simplicity and efficiency.

## Features

- **CPU Load**: Displays the average CPU usage across all cores.
- **Memory Usage**: Displays the percentage of memory in use.
- **Disk Usage**: Provides an overview of disk usage across mounted disks.
- **System Uptime**: Displays how long the system has been running since the last boot.

## Installation

### Requirements

- Python 3.x
- `psutil` library for system metrics

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/sudo-seraphina/moodfetch.git
   cd moodfetch
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
3. Run:
    ```bash
   pip install -e .
4. And finally,
   ```bash
   moodfetch

Rock !!!!

## Usage

moodfetch --verbose (for full details)
moodfetch -default
moodfetch --minimal (for minimal details)

## License
This project is licensed under the MIT License 

## Acknowledgements
The psutil library for providing system metrics.
Inspiration from various system monitoring tools.
