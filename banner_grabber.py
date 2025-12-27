import socket

host = input("Enter target IP: ")
port = int(input("Enter port: "))

s = socket.socket()
s.settimeout(3)

try:
    s.connect((host, port))
    banner = s.recv(1024)
    print("\nBanner:")
    print(banner.decode(errors="ignore"))
except Exception as e:
    print("Error:", e)
finally:
    s.close()
