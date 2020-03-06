import random, requests, json, colorama, time
from colorama import Fore

colorama.init()

def AddConn(name, token, amount):
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    ID = random.randrange(10000000, 90000000)
    for _i in range(amount):
        try:
            time.sleep(10) # 10 seconds sleep time so you dont flood discord requests
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] New connection added!"+Fore.RESET)
            elif 'Unauthorized' in r.text:
                print(f"{Fore.RED}[-] Improper token has been passed!"+Fore.RESET);break
            else:
                print(f"{Fore.RED}[-] Couldnt add connection!"+Fore.RESET);break
        except (Exception, ValueError) as e:
            print(e);break

if __name__ == '__main__':
    print("-----------------------------------")
    name = input("What do you want the name of the connection to be?\n> ")
    token = input("Paste your discord user token here\n> ")
    amount = int(input("How many connections do you want?\n> "))
    print("-----------------------------------")
    AddConn(name, token, amount)
