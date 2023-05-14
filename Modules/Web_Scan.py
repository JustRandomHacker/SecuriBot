import os
import fade
from colorama import Fore, init, Style

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

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


while True:
    # Get the IP or URL of the web application from the user
    url = input("Please enter the IP or URL of the web application: ")

    # Nikto command
    nikto_command = f"nikto -h {url}"

    # Execute Nikto command
    os.system(nikto_command)

    # Ask the user if they want to continue
    continuer = input("Do you want to perform another scan? (yes/no): ")
    if continuer.lower() != "yes":
        # Ask the user if they want to perform a WPScan
        wpscan = input("Do you want to perform a WPScan? (yes/no): ")
        if wpscan.lower() == "yes":
            # WPScan command
            wpscan_command = f"wpscan --url {url}"

            # Execute WPScan command
            os.system(wpscan_command)

        # Quit the script
        break

    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
