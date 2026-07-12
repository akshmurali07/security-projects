# Port Scanner

A Python-based network port scanner that detects open ports on a target host using TCP socket connections.

## What it does
- Scans a range of ports on any target host
- Identifies open ports and their services
- Supports custom port ranges via command line arguments

## Installation
```bash
pip install -r requirements.txt
```

## How to run
```bash
python port-scanner.py --start 1 --end 100
```

## Example Output
![Port Scanner Output](screenshot.png)

## Technologies Used
- Python 3
- Socket programming
- Threading
- Argparse