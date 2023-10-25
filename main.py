# Made by @nicolaspoersch
import requests
import platform
import random
import string
import threading
import keyboard
from colorama import Fore, init
import os
import time

init(autoreset=True)

found_directories = []

def generate_random_user_agent():
    browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera"]
    browser = random.choice(browsers)
    version = str(random.randint(50, 90))
    platform = random.choice(["Windows NT 10.0", "Windows NT 6.1", "Macintosh", "Linux"])
    user_agent = f"Mozilla/5.0 ({platform}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version}.0 Safari/537.36"
    return user_agent

def generate_random_cookie():
    cookie_name = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    cookie_value = "".join(random.choices(string.ascii_letters + string.digits, k=20))
    return f"{cookie_name}={cookie_value}"

def check_directory(directory, cookies, user_agent):
    url = f"https://{target_domain}/{directory.strip()}"
    headers = {"User-Agent": user_agent}
    if cookies:
        headers["Cookie"] = cookies
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(Fore.RED + f"HTTP Request Error: {e}")
        return
    if response.status_code == 200 and not response.url.startswith(f"https://{target_domain}"):
        print(Fore.GREEN + f"[+] Directory Found: {url}")
        found_directories.append(url)

def check_continue():
    while True:
        response = input(Fore.YELLOW + "Do you want to perform another directory scan? (Type 'yes' or 'no'): ")
        if response.lower() == 'yes':
            return True
        elif response.lower() == 'no':
            return False
        else:
            print(Fore.RED + "Invalid response. Please type 'yes' or 'no.")

def stop_program(e):
    global interrupted
    if e.event_type == keyboard.KEY_DOWN:
        if keyboard.is_pressed('ctrl+alt+s'):
            print(Fore.RED + "Scan interrupted by the user.")
            interrupted = True
    return

banner = Fore.RED + """
███████╗ ██████╗██╗  ██╗   ██╗██████╗ ███████╗███████╗
██╔════╝██╔════╝██║  ╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝
█████╗  ██║     ██║   ╚████╔╝ ██████╔╝███████╗█████╗  
██╔══╝  ██║     ██║    ╚██╔╝  ██╔═══╝ ╚════██║██╔══╝  
███████╗╚██████╗███████╗██║   ██║     ███████║███████╗
╚══════╝ ╚═════╝╚══════╝╚═╝   ╚═╝     ╚══════╝╚══════╝
                           
GitHub: https://github.com/nicolaspoersch
"""

print(Fore.YELLOW + "Disclaimer: This program is for ethical and authorized use only. Unauthorized use may be illegal.")
print()
print(banner)

target_domain = input(Fore.YELLOW + "Enter the target domain (e.g., example.com): ")

directories_file = input(Fore.YELLOW + "Enter the name of the text file with the list of directories (e.g., directories.txt): ")

if not directories_file.endswith(".txt"):
    print(Fore.RED + "Error: The text file must have a .txt extension.")
    exit(1)

with open(directories_file, "r") as file:
    directories = file.readlines()

cookie_option = input(Fore.YELLOW + "Do you want to specify a cookie (Type 'y' for yes, 'n' for no): ")
if cookie_option.lower() == 'y':
    cookie = input(Fore.GREEN + "Enter the cookie to be sent with requests (in a format similar to the provided example): ")
else:
    cookie = generate_random_cookie()
    print(Fore.GREEN + f"[+] Generated Cookie: {cookie}")

user_agent_option = input(Fore.YELLOW + "Do you want to specify a custom User-Agent (Type 'y' for yes, 'n' for no): ")
if user_agent_option.lower() == 'y':
    user_agent = input(Fore.GREEN + "Enter the custom User-Agent: ")
else:
    user_agent = generate_random_user_agent()
    print(Fore.GREEN + f"[+] Generated User-Agent: {user_agent}")

target_url = target_domain

print(Fore.LIGHTRED_EX + "\n[+] Starting brute-force. This may take some time. Press 'ctrl+alt+s' at any time to interrupt.")

interrupted = False

keyboard.on_press(stop_program)

for directory in directories:
    if interrupted:
        break
    check_directory(directory, cookie, user_agent)

report_file = "report.txt"

if interrupted:
    with open(report_file, "w") as report:
        report.write("[!] Partial Report - Directories found until interruption:\n")
        for directory in found_directories:
            report.write(f"{directory}\n")
else:
    with open(report_file, "w") as report:
        report.write("[!] Complete Report - All directories found:\n")
        for directory in found_directories:
            report.write(f"{directory}\n")

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print(banner)
print(Fore.LIGHTWHITE_EX + "Thank you for using this tool! If you liked it, consider giving it a star on the GitHub project")
print(Fore.LIGHTWHITE_EX + "This project is open to contributions. Feel free to collaborate and make it even better!")

print(Fore.LIGHTGREEN_EX + f"[!] There is a report at {os.path.abspath(report_file)}.")

for i in range(30, 0, -1):
    print(Fore.LIGHTGREEN_EX + f"The program will close in {i} seconds.", end='\r')
    time.sleep(1)

exit()
