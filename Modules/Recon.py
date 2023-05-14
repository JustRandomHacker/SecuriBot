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

import re
import os
from termcolor import colored

def main():
    while True:
        
        while True:
            network_ip = input(colored("Enter the network IP to scan (e.g. 192.168.0.0): ", "yellow", attrs=["bold"]))
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", network_ip):
                break
            print(colored("Invalid IP entered. Please enter a valid IP address (e.g. 192.168.0.0)", "red", attrs=["bold"]))

        
        while True:
            mask = input(colored("Enter the network mask in CIDR notation (e.g. 24): ", "yellow", attrs=["bold"]))
            if re.match(r"^\d{1,2}$", mask) and int(mask) <= 32:
                break
            print(colored("Invalid network mask entered. Please enter an integer between 1 and 32.", "red", attrs=["bold"]))

        network = f"{network_ip}/{mask}"

        
        os.system(f"nmap -sn {network}")

        
        while True:
            host_ip = input(colored("Enter the IP address of the machine to scan: ", "yellow", attrs=["bold"]))
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host_ip):
                break
            print(colored("The IP address entered is invalid. Please enter a valid IP address (e.g. 192.168.0.1)", "red", attrs=["bold"]))

        
        os.system(f"nmap -p- -sV -oX scan.xml {host_ip}")

        
        while True:
            searchsploit = input(colored("Do you want to perform an exploit search with searchsploit? (yes/no) ", "yellow", attrs=["bold"]))
            if searchsploit in ["yes", "no"]:
                break
            print(colored("Please enter 'yes' or 'no'.", "red", attrs=["bold"]))

        
        if searchsploit == "yes":
            os.system(f"searchsploit -v --nmap scan.xml")

        
        while True:
            restart = input(colored("Do you want to restart the scan? (yes/no) ", "yellow", attrs=["bold"]))
            if restart in ["yes", "no"]:
                break
            print(colored("Please enter 'yes' or 'no'.", "red", attrs=["bold"]))

        if restart != "yes":
            break

if __name__ == "__main__":
    main()
