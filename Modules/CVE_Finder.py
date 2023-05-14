import requests
import os
import fade
from colorama import init, Fore, Style

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

while True:
    clear()

    print("")
    faded_text = fade.purplepink(banner)
    print(faded_text)

    print(Fore.GREEN + " 	    	   Created by github/JustRandomHacker")
    print("")

    service = input("Enter service name : ")

    url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?keyword={service}&resultsPerPage=100"

    response = requests.get(url)

    if response.status_code == 200:
        results = response.json().get("result").get("CVE_Items")
        if len(results) > 0:
            sorted_results = sorted(results, key=lambda x: x.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('baseSeverity', 'N/A'), reverse=True)
            for result in sorted_results:
                cve = result.get("cve")
                cve_id = cve.get('CVE_data_meta').get('ID')
                severity = result.get('impact', {}).get('baseMetricV3', {}).get('cvssV3', {}).get('baseSeverity', 'N/A')
                description = cve.get('description', {}).get('description_data', [{}])[0].get('value', 'N/A')
                print(f"{Fore.GREEN}CVE ID:{Style.RESET_ALL} {cve_id:<20} {Fore.RED}Severity:{Style.RESET_ALL} {severity:<10} {Fore.YELLOW}Description:{Style.RESET_ALL} {description}")
        else:
            print(f"No results found for {service}")
    else:
        print("An error occured. Please try again.")
    
    response = input("Would you like to find another CVE ? (yes/no) : ")
    if response.lower() == "no":
        break
