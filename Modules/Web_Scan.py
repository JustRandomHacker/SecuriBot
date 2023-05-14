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

def print_question(question):
    print(f"\033[1m\033[95m{question}\033[0m")

while True:
    
    print_question("Please enter the IP or URL of the web application: ")
    url = input()

    
    nikto_command = f"nikto -h {url}"

    
    os.system(nikto_command)

    
    print_question("Do you want to perform another scan? (yes/no): ")
    continuer = input()
    if continuer.lower() != "yes":
        
        print_question("Do you want to perform a WPScan? (yes/no): ")
        wpscan = input()
        if wpscan.lower() == "yes":
            
            wpscan_command = f"wpscan --url {url}"

            
            os.system(wpscan_command)

        
        break

    
    os.system('cls' if os.name == 'nt' else 'clear')
