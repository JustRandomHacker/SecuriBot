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
    print("*********************************")
    print("[ 1 ] - RECON                   *")
    print("[ 2 ] - WEB APP SCANNER         *")
    print("[ 3 ] - OSINT / SHODAN          *")
    print("[ 4 ] - CVE FINDER              *")
    print("[ 5 ] - PASSWORD CHECKER        *")
    print("[ 6 ] - SQL INJECTION           *")
    print("[ 7 ] - Exit                    *")
    print("*********************************")
    choix = input("Select your option: ")
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
        print("Thanks for using my script :D, have a nice day !")
        break
    else:
        print("Wrong option. Please, use a correct option (1 to 5).")
