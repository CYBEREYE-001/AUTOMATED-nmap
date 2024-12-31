Nmap Scan Automation Script

This Python script provides a simple and user-friendly interface to perform network scans using Nmap. It allows users to choose between SYN scan, TCP scan, or a full scan, targeting specific ports or all ports on a specified IP address.

Features

User Input for Target IP: Prompts the user to input the IP address of the target machine.

Scan Type Selection:

Press 1 for a SYN scan.

Press 2 for a TCP scan.

Press 3 for a full scan.


Custom Port Scanning: Allows the user to specify a particular port to scan (for SYN and TCP scans).

Detailed Output: Includes service detection (-sV) and operating system detection (-O) in all scan types.


Prerequisites

Python 3: Make sure Python 3 is installed on your system.

Nmap: Install Nmap on your machine to execute the scans.


Usage

1. Run the script:

python3 nmap_scan.py


2. Follow the prompts:

Enter the target IP address.

Select the scan type by entering 1, 2, or 3.

Specify the target port (if applicable).




Code Explanation

Line 1: Imports the subprocess module to execute Nmap commands from the script.

Line 2-3: Takes input for the target IP address and scan type.

Line 4-5: Prompts for the target port if a SYN or TCP scan is selected.

Line 6-11: Executes the appropriate Nmap scan based on the user's input.


Note

This script requires administrative privileges to execute certain scans. Make sure you run it with the necessary permissions.
