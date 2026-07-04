import socket

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

host = "scanme.nmap.org"
for port in range(20, 25):
    scan_port(host, port)