# Nmap Wrapper

## Overview
The Nmap Wrapper is a Python tool that runs Nmap scans via the `subprocess` module and captures the output. It simplifies executing Nmap commands with custom options and logs the results.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- Nmap installed on the system (`sudo apt install nmap` or equivalent)
- Appropriate permissions for Nmap (often requires root)

## Usage
Run the script with the following arguments:

```bash
python3 nmap_wrapper.py --target <TARGET> [--options <OPTIONS>] [--config <CONFIG_FILE>]
