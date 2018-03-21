# scripts
Main purpose of the project is to research and develop
monitoring scripts for some servers that run BOINC &
for old notebook of my favourite Mother:)

She uses now Lubuntu 16.04 LTS + 4G-modem for Skype whith me and family.
3G-4F usually has dynamic IP ,so - communications via email 
NOTE: some ISP want to put these mails in spam, search and unmark them

Also tested in Ubuntu 17.04, Debian 9

Usually to start monitoring i need 3 files:
1.main script report.py installed in ~/DO
It starts on @reboot by cron 

2. report.py needs no changes, if network exists-execute ~/DO/monitor.py,
if not- sleeps and do cycle until network appears. (may depend on ping version)

3. in monitor.py i need to change string 'filename' of additional command file to load 
(name depends on host)
Command file will download from repository and execute

4.If necessary I can put additional commands to file task_{host}.py
and get additional reports by mail (different commans for different hosts)
or stay it empty

TODO:
- put pure commands to task_{host}.py without python code(use pure bash, but python present everywhere)
