import random, requests, json, time
from colorama import Fore

init(convert=True)

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
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            elif 'Unauthorized' in r.text:
                print(f"[{Fore.RED}-{Fore.RESET}] Improper token has been passed!");break
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break

if __name__ == '__main__':
    print("-----------------------------------")
    name = input("What do you want the name of the connection to be?\n> ")
    token = input("Paste your discord user token here\n> ")
    amount = int(input("How many connections do you want?\n> "))
    print("-----------------------------------")
    time.sleep(3)
    AddConn(name, token, amount)
