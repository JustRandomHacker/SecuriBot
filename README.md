# <div align="center"> SecuriBot
<p align="center">
  <img src="https://img.shields.io/badge/python-v3.11.2-green">
  <img src="https://img.shields.io/badge/version-1.0-blue">
  <p>

"SecuriBot" is a Python-based security tool designed for automated scanning of target systems. It boasts a variety of powerful features and tools specifically tailored for penetration testing purposes.

## 📢 Description

SecuriBot is a security tool designed to automate repetitive tasks performed by SOC analysts. As an SOC analyst, certain tasks can become tedious and time-consuming. The main objective of this project is to search and collect specific information that can be used to automate security actions. The ultimate goal of this project is to create a playbook of automated tasks (i.e., "toolbox") for RED TEAM operations. 

SecuriBot simplifies the process of automating these tasks, making the analyst's job more efficient and effective.

## ⚠️ Disclaimer
This cybersecurity toolbox is intended for educational and ethical hacking purposes only. Any unauthorized or illegal use of this tool is strictly prohibited. The author of this tool will not be held responsible for any damages or illegal actions caused by the use of this toolbox. It is the user's responsibility to ensure that they are in compliance with all applicable laws and regulations. Use at your own risk.

## 📁 Installation 

### Kali Linux / Python 
This toolbox was developed on a Kali Linux distribution and coded in Python version 3.11.2. 
To avoid any compatibility issues, please execute this script on a Kali Linux environment with an up-to-date version of Python.

Otherwise, please install Python from the official website: https://www.python.org/downloads/

Kali Linux can be found at : https://www.kali.org/get-kali/#kali-platforms

### Download & Install 
To begin, you must download the repository. To do so, execute the following commands on your Kali machine:
```
git clone https://github.com/JustRandomHacker/SecuriBot.git
```
Once the archive has been downloaded, navigate to the directory and install the prerequisites to ensure that the script runs correctly:
```
cd SecuriBot
pip install -r requirements.txt
```
## 🎯 Features 
- <strong>Comprehensive network reconnaissance tool (Nmap)</strong> ✔️
- <strong>Ability to view all active hosts on a network</strong> ✔️
- <strong>Ability to view all open TCP ports on a host</strong> ✔️
- <strong>CVE search tool (Searchsploit)</strong> ✔️
- <strong>Web application vulnerability scanner (Nikto / WPScan)</strong> ✔️
- <strong>OSINT tool (Shodan)</strong> ✔️
- <strong>Password leak checker (HaveIBeenPwned)</strong> ✔️
- <strong>Robust password generator</strong> ✔️
- <strong>Automatic SQL injection (GET request only)</strong> ✔️
- <strong>Extremely user-friendly and easy to use</strong> ✔️

## 📷 Screenshots
![securibot](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/f383cafc-465a-4a0b-bb08-516d10405655)

### 👀 Recon 
![RECON](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/575d9fc5-6344-4e12-9200-cde03bdb615d)
### ⚡ Web App Scanner
![webapp](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/9560b0e1-064b-4e0c-baf6-12b773a6f257)
### 🔍 OSINT
![SHODAN](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/4170da10-f7c2-4ec2-9bb1-87db50249d5b)
### 📋 CVE Finder
![CVE](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/b9bd6f6a-3727-49c2-a054-63bb2fb79f0e)
### 🔑 Password Checker
![PASSWORD](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/cfd37145-f657-4ee0-9a64-5e64488c690f)
### 💉 SQLi 
![sqli1](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/ca0386e5-21df-448f-aad7-5a54430e32f8)
![sqli2](https://github.com/JustRandomHacker/SecuriBot/assets/120188003/d785fc1e-6a36-420c-9f01-418f8f883e49)

## 📝 How to use SecuriBot
Once you have downloaded and installed the prerequisites, you will need to navigate to the SecuriBot directory, open a terminal, and simply run the following command:
```
python SecuriBot.py
```
Once completed, a menu will appear, allowing you to select the desired module by simply entering the corresponding number (1 to 7).

```
           
░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗██████╗░░█████╗░████████╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║██████╦╝██║░░██║░░░██║░░░
░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║██╔══██╗██║░░██║░░░██║░░░
██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░  

                   Created by github/JustRandomHacker

*********************************
[ 1 ] - RECON                   *
[ 2 ] - WEB APP SCANNER         *
[ 3 ] - OSINT / SHODAN          *
[ 4 ] - CVE FINDER              *
[ 5 ] - PASSWORD CHECKER        *
[ 6 ] - SQL INJECTION           *
[ 7 ] - Exit                    *
*********************************
Select your option: 
```
## ✍️ Author
This project was entirely developed by <strong>JustRandomHacker</strong> and is completely free to use.

Don't hesitate to give me feedback if you enjoyed the project! It was a fun project for me to work on :D
