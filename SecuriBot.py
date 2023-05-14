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
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
print("")
faded_text = fade.purplepink(banner)
print(faded_text)

print(colors.BOLD + colors.DARKCYAN + " 	    	   Created by github/JustRandomHacker")
print("")

while True:
    print(colors.BOLD + colors.PURPLE + "*********************************" + colors.END)
    print(colors.BOLD + colors.PURPLE + "[ 1 ] - RECON                   *" + colors.END)
    print(colors.BOLD + colors.PURPLE + "[ 2 ] - WEB APP SCANNER         *" + colors.END)
    print(colors.BOLD + colors.PURPLE + "[ 3 ] - OSINT / SHODAN          *" + colors.END)
    print(colors.BOLD + colors.PURPLE + "[ 4 ] - CVE FINDER              *" + colors.END)
    print(colors.BOLD + colors.PURPLE + "[ 5 ] - PASSWORD CHECKER        *" + colors.END)
    print(colors.BOLD + colors.PURPLE + "[ 6 ] - SQL INJECTION           *" + colors.END)
    print(colors.BOLD + colors.RED + "[ 7 ] - Exit                    *" + colors.END)
    print(colors.BOLD + colors.PURPLE + "*********************************" + colors.END)
    
    
    choix = input(colors.BOLD + "Select your option: " + colors.END)
    
    
    if choix == "1":
        os.system("python Modules/Recon.py")
    elif choix == "2":
        os.system("python Modules/Web_Scan.py")
    elif choix == "3":
        os.system("python Modules/Osint.py")
    elif choix == "4":
        os.system("python Modules/CVE_Finder.py")
    elif choix == "5":
        os.system("python Modules/Password_Checker.py")
    elif choix == "6":
        os.system("python Modules/SQLi.py")   
    elif choix == "7":
        print("")
        print(colors.BOLD + "Thanks for using my script :D, have a nice day !" + colors.END)
        break
    else:
        print(colors.BOLD + colors.RED + "Wrong option. Please, use a correct option (1 to 7)." + colors.END)
