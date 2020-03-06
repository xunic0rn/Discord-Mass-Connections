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
                print("New connection added!")
            else:
                print("Couldnt add connection :(")  
        except Exception as e:
            print(e)
        else:
            print(r.text);break

if __name__ == '__main__':
    print("-----------------------------------")
    name = input("What do you want the name of the connection to be?\n> ")
    token = input("Paste your discord user token here\n> ")
    amount = int(input("How many connections do you want?\n> "))
    print(f"{Fore.RED}WARNING: {Fore.RESET}Close this program when you feel like you have enough connections!")
    print("-----------------------------------")
    AddConn(name, token, amount)
