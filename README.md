🅽🅼🅰🅿 🆂🅲🅰🅽 🅰🆄🆃🅾🅼🅰🆃🅸🅾🅽 🆂🅲🆁🅸🅿🆃

This Python script provides a simple and user-friendly interface to perform network scans using Nmap. It allows users to choose between SYN scan, TCP scan, or a full scan, targeting specific ports or all ports on a specified IP address.

F⃣   e⃣   a⃣   t⃣   u⃣   r⃣   e⃣   s⃣ :

User Input for Target IP: Prompts the user to input the IP address of the target machine.

s⃣   c⃣   a⃣   n⃣    t⃣   y⃣   p⃣   e⃣    s⃣   e⃣   l⃣   e⃣   c⃣   t⃣   i⃣   o⃣   n⃣ :

Press 1 for a SYN scan.

Press 2 for a TCP scan.

Press 3 for a full scan.


ℂ𝕦𝕤𝕥𝕠𝕞 ℙ𝕠𝕣𝕥 𝕊𝕔𝕒𝕟𝕟𝕚𝕟𝕘: Allows the user to specify a particular port to scan (for SYN and TCP scans).

𝔻𝕖𝕥𝕒𝕚𝕝𝕖𝕕 𝕆𝕦𝕥𝕡𝕦𝕥: Includes service detection (-sV) and operating system detection (-O) in all scan types.


ℙ𝕣𝕖𝕣𝕖𝕢𝕦𝕚𝕤𝕚𝕥𝕖𝕤 -

#Python 3: Make sure Python 3 is installed on your system.

#Nmap: Install Nmap on your machine to execute the scans.


U⃣   s⃣   a⃣   g⃣   e⃣ :

1. Run the script:

python3 nmap_scan.py


2. Follow the prompts:

Enter the target IP address.

Select the scan type by entering 1, 2, or 3.

Specify the target port (if applicable).

Note

This script requires administrative privileges to execute certain scans. Make sure you run it with the necessary permissions.
