import requests
import hashlib
import random
import string
import requests
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

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password = input("\033[1mPlease enter your password to test:\033[0m ")
    count = pwned_api_check(password)
    if count:
        print(f"\033[1mThe password '{password}' has been found {count} times in data breaches and is therefore compromised.\033[0m")
        choice = input("\033[1mWould you like to generate a new secure password? (Y/N):\033[0m ")
        if choice.lower() == 'y':
            new_password = generate_password()
            new_count = pwned_api_check(new_password)
            while new_count:
                new_password = generate_password()
                new_count = pwned_api_check(new_password)
            print(f"\033[1mThe new secure password is: {new_password}\033[0m")
        else:
            print("\033[1mPlease change your compromised password.\033[0m")
    else:
        print(f"\033[1mThe password '{password}' has not been found in data breaches and is therefore safe.\033[0m")

if __name__ == '__main__':
    main()
