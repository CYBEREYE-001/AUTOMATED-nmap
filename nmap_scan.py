import subprocess
ip=input("ENTER THE VICTIM IP ADDRESS: ")
scan=int(input("PRESS \n 1 = SYN SCAN \n 2 = TCP SCAN \n 3 = FULL SCAN \n ENTER = "))
if scan in [1, 2]:
    port=input("SPECIFY THE PORT WHAT DO YOU WANT TO SCAN: ")
if scan == 1:
    subprocess.run(["nmap", ip, "-p", port, "-sS", "-sV", "-O"])
elif scan == 2:
    subprocess.run(["nmap", ip, "-p", port, "-sT", "-sV", "-O"])
else:
    subprocess.run(["nmap", ip, "-sV", "-O"])