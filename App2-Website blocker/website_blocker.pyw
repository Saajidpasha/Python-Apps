#saving file as pyw will run script in bakgrnd
#open task scheduler and create a new task website blocker
#configure for windows 10
#run with high privilages
#triggers upon start
#actions= browse script location

import time
from datetime import datetime as dt

website_list = ["www.facebook.com","facebook.com","www.hotmail.com"]
host_temp = "hosts"
host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9):
        print("Working hourss...")
        with open(host_temp,"r+") as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_temp,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours..")
    time.sleep(5)
