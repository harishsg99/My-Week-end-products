# to run the program on the backside change file extension from .py to .pyw
import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.yahoo.com","yahoo.com"]
# copy hosts file from address to coding folder or wherever blocker.py resides
# create copies of host file in another folder to avoid problems due to loss 
# necessary file in case of wrong execution for some reason, 
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open("hosts_temp","r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open("hosts_temp","r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()        
        print("Fun hours.....")
        time.sleep(5)                