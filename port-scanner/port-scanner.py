import socket
import argparse

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

# This part reads what you type in the terminal
parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=1)
parser.add_argument("--end", type=int, default=100)
args = parser.parse_args()

host = "scanme.nmap.org"
print(f"Scanning ports {args.start} to {args.end}...")

for port in range(args.start, args.end + 1):
    scan_port(host, port)

print("Done!")