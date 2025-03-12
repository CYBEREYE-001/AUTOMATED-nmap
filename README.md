# Network Port Scanner

This Python script is a simple yet powerful network port scanner that utilizes Nmap to perform various types of scans on a specified target IP address. It allows users to specify individual ports, ranges of ports, or scan all ports, and offers options for service version detection and OS detection.

## Features

- **IP Address Validation**: Ensures that the provided IP address is in a valid format.
- **Port Input Handling**: Accepts single ports, multiple ports, or ranges of ports for scanning.
- **Multiple Scan Types**: Offers various scanning techniques, including:
  - SYN Scan (`-sS`)
  - TCP Connect Scan (`-sT`)
  - Full Scan (defaulting to SYN Scan)
  - FIN Scan (`-sF`)
  - Xmas Scan (`-sX`)
  - NULL Scan (`-sN`)
  - UDP Scan (`-sU`)
- **Service Version Detection**: Optionally includes service version detection with the `-sV` flag.
- **OS Detection**: Optionally includes OS detection with the `-O` flag.
- **Command Execution**: Executes the Nmap command directly from the script and displays the command being run.

## Requirements

- Python 3.x

  ```bash
  apt install python3-full
  ```
- Nmap installed on your system

  ```bash
  apt install nmap
  ```
- figlet installed on your system
  
  ```bash
  apt install figlet
  ```
- If you are using ARCH linux then replace the "apt install" and use "pacman -S"
  
## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/CYBEREYE-001/AUTOMATED-nmap.git
   cd AUTOMATED-nmap
   ```

2. Run the script:
   ```bash
   python3 nmap_scan.py
   ```

3. Follow the prompts to enter the target IP address, select the scan type, and specify the ports to scan.

## Example

```plaintext
ENTER THE VICTIM IP ADDRESS: 192.168.1.1
PRESS:
1 = SYN SCAN
2 = TCP CONNECT SCAN
3 = FULL SCAN
4 = FIN SCAN
5 = Xmas SCAN
6 = NULL SCAN
7 = UDP SCAN
ENTER YOUR CHOICE: 1
SPECIFY THE PORT(S) (e.g., 22, 80, 100-200) or press Enter to scan all ports: 22, 80
Include service version detection? (y/n): y
Include OS detection? (y/n): n
Executing command: nmap 192.168.1.1 -sS -sV -p 22 80
```

## Notes

- Ensure you have the necessary permissions to scan the target IP address.
- Use responsibly and only scan networks you own or have explicit permission to test.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify any part of the description to better fit your style or the specifics of your project!
