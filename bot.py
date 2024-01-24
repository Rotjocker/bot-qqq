import requests,threading,random,sys,time,os
import requests,threading,random,sys,time,os
requests.packages.urllib3.disable_warnings()
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر

igu = "1308075085"
toku= "5877866725:AAGUQ82KwEaSn_oPWKJHiJvpkl6k3P6Pfqs"
os.system('clear')
import random
abc ='qwertyuioplkjhgfdsazxcvbnm1234567890'
abc1 ='._'

proxy= requests.get('https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&_ga=2.192911210.1550271373.1705606782-83141249.1705606782').text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()
class tiktok:
	def __init__(self):
		print("""\033[1m
           
		""")
		try:
			self.length = ''
		except :
			self.length = 4

	def Checker(self):
		while True:
			abc ='qwertyuioplkjhgfdsazxcvbnm1234567890'
			abc1 ='_'
			abc2='.'
			v1 = str(''.join((random.choice(abc) for i in range(1))))
			v2=str("".join(random.choice(abc1)for i in range(1)))
			v3=str("".join(random.choice(abc2)for i in range(1)))
			v4 = str(''.join((random.choice(abc) for i in range(1))))
			v5 = str(''.join((random.choice(abc) for i in range(1))))
			v6 = str(''.join((random.choice(abc) for i in range(1))))
			user1 = (v1+v4+v5+v2)
			user2 = (v1+v2+v4+v5)
			user3 = (v1+v4+v2+v5)
			user4 = (v2+v1+v1+v1)
			user6 = (v1+v3+v4+v5)
			user7 = (v4+v5+v3+v1)
			user8 = (v5+v1+v2+v6)
			user9 = (v2+v1+v3+v4)
			user10 = (v2+v1+v2+v6)
			user11 = (v2+v3+v3+v1)
			user12 = (v6+v3+v1+v4)
			user13 = (v2+v1+v1)
			user14 = (v1+v3+v5)

			hamo010 = (user1, user2, user3, user4, user6, user7, user8, user9, user10, user11, user12, user13, user14)
			username = random.choice(hamo010)
			url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"
			headers = {
				'User-Agent':'TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4',
				'x-rapidapi-key':'d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77'
			}
			
			if username.isnumeric():
				pass
			else:
				response = requests.get(url,headers=headers,allow_redirects=False,verify=False,proxies={'http': 'http://' + random.choice(s)})
				if "user does not exist" in response.text:
					print("-"*40)
					print(f"\033[1;32m available : {username}")
					print("-"*40)
					tlgu= (f'''GOOD USER ✔️\nUSER : {username}''')
					requests.get("https://api.telegram.org/bot"+str(toku)+"/sendMessage?chat_id="+str(igu)+"&text="+str(tlgu))
                                        
					
					with open('tiktok.txt','a') as f:
						f.write(f"{username}\n")
				elif "unique_id" in response.text:
					print(f" \033[1;31munavailable : {username}")
				elif "API" in response.text:
					print(" \033[1;33m IP banned ")
					time.sleep(10)
				else:
					print(response.text)
					with open('unknown.txt','a') as f:
						f.write(f'{username}\n')
tiktok = tiktok()

for _ in range(10):
	threading.Thread(target=tiktok.Checker).start()