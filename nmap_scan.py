import subprocess
import re

subprocess.run(["figlet", "AUTO-NMAP"])
print(">>--S-T-A-R-T-E-D--<<")

def is_valid_ip(ip):
    """Validate the IP address format."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

def is_valid_port(port):
    """Validate the port number."""
    return port.isdigit() and 1 <= int(port) <= 65535

def get_ports():
    """Get ports from the user, allowing for a single port, multiple ports, or a range."""
    ports_input = input("SPECIFY THE PORT(S) (e.g., 22, 80, 100-200) or press Enter to scan all ports: ")
    ports = set()
    if ports_input.strip() == "":
        return "1-65535"  # Return a string indicating to scan all ports
    for part in ports_input.split(','):
        part = part.strip()
        if '-' in part:
            start, end = part.split('-')
            if is_valid_port(start) and is_valid_port(end):
                ports.update(range(int(start), int(end) + 1))
            else:
                print(f"Invalid port range: {part}")
        elif is_valid_port(part):
            ports.add(int(part))
        else:
            print(f"Invalid port: {part}")
    return sorted(ports)

def main():
    # Get the target IP address from the user
    ip = input(">> ENTER THE VICTIM IP ADDRESS: ")
    if not is_valid_ip(ip):
        print("Invalid IP address format.")
        return

    # Display scan options and get the user's choice
    print("PRESS:")
    print("> 1 = SYN SCAN")
    print("> 2 = TCP CONNECT SCAN")
    print("> 3 = FULL SCAN")
    print("> 4 = FIN SCAN")
    print("> 5 = Xmas SCAN")
    print("> 6 = NULL SCAN")
    print("> 7 = UDP SCAN")
    scan = input("ENTER YOUR CHOICE: ")

    # Get the ports to scan
    ports = get_ports()

    # Options for service version and OS detection
    options = []
    if input("Include service version detection? (y/n): ").lower() == 'y':
        options.append("-sV")
    if input("Include OS detection? (y/n): ").lower() == 'y':
        options.append("-O")

    # Execute the corresponding Nmap command based on the user's choice
    command = ["nmap", ip]
    
    if scan == '1':  # SYN SCAN
        command += ["-sS"] + options
    elif scan == '2':  # TCP CONNECT SCAN
        command += ["-sT"] + options
    elif scan == '3':  # FULL SCAN (using SYN SCAN by default)
        command += ["-sS"] + options
    elif scan == '4':  # FIN SCAN
        command += ["-sF"] + options
    elif scan == '5':  # Xmas SCAN
        command += ["-sX"] + options
    elif scan == '6':  # NULL SCAN
        command += ["-sN"] + options
    elif scan == '7':  # UDP SCAN
        command += ["-sU"] + options
    else:
        print("Invalid choice. Please select a valid scan type.")
        return

    # Add ports to the command
    if isinstance(ports, str):  # If ports is a string, it indicates to scan all ports
        command += ["-p", ports]
    else:
        command += ["-p"] + [str(port) for port in ports]

    # Execute the Nmap command
    print("Executing command:", " ".join(command))
    subprocess.run(command)

if __name__ == "__main__":
    main()
