#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
#Prog:from cron and if network exists
#load external module chunk.py, chmod it to a+x and execute
# for monitoring outstanding server\workstation
#Author: vasily122@pisem.net
#Date: 2015 nov 7
# Version: 0.1
#====================================
import time,os
kanal=0
#print("===start===")

while kanal==0:
#	print("+\n")
#	time.sleep(3)
	b=os.popen("ping -c1 8.8.8.8").read()
	if(b[68:77] =="icmp_seq="):
		kanal=1


os.system("wget https://raw.githubusercontent.com/vasily122/scripts/master/chunk.py")
os.system("chmod a+x chunk.py && ./chunk.py")

#os.system("rm chunk.py")
#os.system("./chunk.py >> out.txt")
#os.system("cp /home/arina122/DO/chunk.py .")
#os.system("chmod a+x chunk.py && ./chunk.py")
#os.system("pwd>>position.txt")

#print("""(uname -a && uptime -p && df) | mail -s "new report" vasily122@yandex.ru""")
