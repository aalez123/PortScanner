import socket
from datetime import datetime

# Function to perform the scan
def port_scan(target, start_port, end_port):
    # Print the starting time
    print(f"Starting scan on {target}")
    print(f"Time started: {datetime.now()}")
    
    # Try connecting to each port in the specified range
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Try to connect to the port
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        # Close the socket connection
        sock.close()

# Input target and port range
if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    port_scan(target, start_port, end_port)
