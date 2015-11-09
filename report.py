#!/usr/bin/python
# -*- coding: utf-8 -*- 
import time,os
kanal=0
while kanal==0:
	time.sleep(300)
	b=os.popen("ping -c1 8.8.8.8").read()
	if(b[68:77] =="icmp_seq="):
		kanal=1
os.system("""(uname -a && date && df) | mail -s "Activity report" vasily122@yandex.ru""")
