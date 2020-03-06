import random, requests, json, colorama, time
from colorama import Fore

colorama.init()

ID  = random.randrange(10000000, 90000000)

print("-----------------------------------")
name = input("What do you want the name of the connection be?\n>")
token = input("Paste your discord user token here\n>")
time.sleep(3)
print(f"{Fore.RED}WARNING: {Fore.RESET}Close this program when you feel like you have enough connections!")
print("-----------------------------------")
time.sleep(5)

payload = {
    'name': name,
		'visibility': 1
}
headers = {
		'Authorization': token,
    'Content-Type':'application/json', 
}

while True:
  try:
     r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{type}/{ID}', data=json.dumps(payload), headers=headers)
     if r.status_code == 200:
         print("New connection added!")
     else:
         print("Couldnt add connection :(")  
  except Exception as e:
          print(e)
  else:
     break 
