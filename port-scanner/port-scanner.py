import socket
import threading

open_ports = []
lock = threading.Lock()

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            with lock:
                open_ports.append(port)
                print(f"Port {port}: OPEN")
        sock.close()
    except:
        pass

host = "scanme.nmap.org"
threads = []
print(f"Scanning {host}...")

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(host, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nOpen ports: {sorted(open_ports)}")