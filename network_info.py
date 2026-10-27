"""Display basic network configuration for the current device."""
import platform
import socket

def main():
    print("CYBER LEARNING LAB | Basic Device Network Info")
    print("Operating system:", platform.platform())
    print("Device hostname:", socket.gethostname())
    try:
        # Uses the system resolver to identify the local address associated
        # with the current hostname; this is not a port scan.
        addresses = sorted({
            item[4][0]
            for item in socket.getaddrinfo(socket.gethostname(), None)
            if item[4] and ":" not in item[4][0]
        })
        print("Resolved IPv4 address(es):", ", ".join(addresses) if addresses else "Not available")
    except socket.gaierror:
        print("Resolved IPv4 address(es): Not available")
    print("For full network details, use your operating system's network settings.")

if __name__ == "__main__":
    main()
