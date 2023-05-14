import os
import re
import fade
from colorama import Fore, init, Style

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name in ("ce", "nt", "dos"):
        os.system("cls")

banner = """
░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗██████╗░░█████╗░████████╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║██████╦╝██║░░██║░░░██║░░░
░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║██╔══██╗██║░░██║░░░██║░░░
██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
"""

clear()

print("")
faded_text = fade.purplepink(banner)
print(faded_text)

print(Fore.GREEN + " 	    	   Created by github/JustRandomHacker")
print("")

def main():
    while True:
        # Ask the user for the network IP to scan and validate it
        while True:
            network_ip = input("Enter the network IP to scan (e.g. 192.168.0.0): ")
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", network_ip):
                break
            print("Invalid IP entered. Please enter a valid IP address (e.g. 192.168.0.0)")

        # Ask the user for the network mask and validate it
        while True:
            mask = input("Enter the network mask in CIDR notation (e.g. 24): ")
            if re.match(r"^\d{1,2}$", mask) and int(mask) <= 32:
                break
            print("Invalid network mask entered. Please enter an integer between 1 and 32.")

        network = f"{network_ip}/{mask}"

        # Perform host discovery
        os.system(f"nmap -sn {network}")

                # Ask the user for the IP of the machine to scan and validate it
        while True:
            host_ip = input("Enter the IP address of the machine to scan: ")
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host_ip):
                break
            print("The IP address entered is invalid. Please enter a valid IP address (e.g. 192.168.0.1)")

        # Launch port scan with XML output
        os.system(f"nmap -p- -sV -oX scan.xml {host_ip}")

        # Ask the user if they want to perform an exploit search with searchsploit
        while True:
            searchsploit = input("Do you want to perform an exploit search with searchsploit? (yes/no) ")
            if searchsploit in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        # If the user chooses to perform the exploit search, run it from the XML file
        if searchsploit == "yes":
            os.system(f"searchsploit -v --nmap scan.xml")

        # Ask the user if they want to restart the script
        while True:
            restart = input("Do you want to restart the scan? (yes/no) ")
            if restart in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if restart != "yes":
            break

if __name__ == "__main__":
    main()


       
