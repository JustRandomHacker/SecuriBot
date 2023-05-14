import os
from colorama import Fore, init, Style
import fade
from shodan import Shodan
import json
import requests
import time
import socket

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

api = Shodan('mEuInz8UH1ixLGJq4oQhEiJORERVG5xc')   


while True:
    clear()
    print("")
    faded_text = fade.purplepink(banner)
    print(faded_text)

    print(Fore.GREEN + " 	    	   Created by github/JustRandomHacker")
    print("")

    print("")
    domain_name = input("Enter domain name or IP address: ")
    IP = socket.gethostbyname(domain_name)
    print(f"The IP address of {domain_name} is {IP}")
    print("Invalid or unresolved domain name")
    clear()
    print("")
    faded_text = fade.purplepink(banner)
    print(faded_text)

    print(Fore.GREEN + " 	    	   Created by github/JustRandomHacker")
    print("")

    print("")
    print(" [+] Connecting to the API ...")

    api2 = f"http://ip-api.com/json/{IP}"
    shodanIP = api.host(IP)

    data = requests.get(api2).json()

    clear()

    print("")

    faded_text = fade.purplepink(banner)
    print(faded_text)

    domain = format(shodanIP.get('hostnames'))
    chars = ['[', ']', "'"]
    res = domain.translate(str.maketrans('', '', ''.join(chars)))

    ports = format(shodanIP.get('ports'))
    chars = ['[', ']', "'"]
    portstext = ports.translate(str.maketrans('', '', ''.join(chars)))

    print(Fore.GREEN + " 	    	   Created by github/JustRandomHacker")
    print("")
    print("")
    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ IP INFORMATION ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ")
    print("")
    print(' [!] IP Address: ', data['query'])
    print(' [!] Status: ', data['status'])
    print(' [!] Country: ', data['country'])
    print(' [!] Country Code: ', data['countryCode'])
    print(' [!] Region: ', data['region'])
    print(' [!] Region Name: ', data['regionName'])
    print(' [!] City: {}'. format(shodanIP.get('city')))
    print(' [!] Zip: ', data['zip'])
    print(' [!] Latitude: ', data['lat'])
    print(' [!] Loginth', data['lon'])
    print(' [!] Time zone: ', data['timezone'])
    print(' [!] IPS: ', data['isp'])
    print(f" [!] Domains: {res}")
    print(' [!] Organization: ', data['org'])
    print(' [!] AS: ', data['as'])
    print(f' [!] Ports: {portstext}')
    print("")
    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("")
    print("")
    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ POSSIBLE EXPLOITS ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("")
    vulns = format(shodanIP.get('vulns', '                      N/A'))
    chars = ['[', ']', "'"]
    vulnstext = vulns.translate(str.maketrans('', '', ''.join(chars)))
    print(f' {vulnstext}')
    print("")
    print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

    user_choice = input("Do you want to test another IP? (y/n) ")

    if user_choice.lower() == "n":
        break

print("Exiting script...") 
