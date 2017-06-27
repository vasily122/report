# scripts
Main purpose of the project is to research and develop
monitoring scripts for some servers that run BOINC &
for old notebook of my favourite Mother:)

She uses Lubuntu 12.04lts + 3G-modem for skype whith me and family.
3G usually has dynamic IP -no ssh, so - communications via email only on reboot

NOTE: some ISP want to put these mails in spam...

Also tested in Ubuntu 16.04, 17.04, Debian...

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
- put pure commands to task_{host}.py without python code
