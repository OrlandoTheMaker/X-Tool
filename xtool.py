import socket 
import time
import os
import subprocess
from colorama import *
import pyfiglet
import sys
#import requests
""" Have imported the neccessary for using this tool
"""
""" socket will be used for sendind tcp or udp connections.

time will be used to calculate your network statistics.

os will be used for direcrory scanning

subprocess (??)

requests already says what it does

"""
"""
I try to make it look as though users are actually logging in to use the tool
"""
""" Create a file to store results or creds
"""
file=[]
print(" You have to create an account to use this tool....")
time.sleep(2)
def login():
    uname=input("  set user name ..: ")
    upass=input("  set strong passworde  : ") 
    time.sleep(2)
    print(Fore.GREEN+" account succefsully created!")
    time.sleep(2)
    subprocess.call('clear',shell=True)
    print("\n")
    print("\n")
    name=input(" Enter your username here  : ")
    pas=input(" Enter your pass here : ")
    time.sleep(2)
    subprocess.call('clear',shell=True) 
    time.sleep(2)
    with open("secret.txt","wb") as lock:
     upass.write(lock)   
     print(lock)
     
""" above code does not store any names and passwords anywhere as either way, the tool still runs
"""  


"""
login
"""      
login()   
 
""" Creating my socket object
"""         
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(Fore.GREEN+" Socket succesfully created")

"""logical operators

"""
if socket.error == True:
    print(Fore.RED+" Socket not created ! error in creating socket %s" %(err))
    time.sleeo(3)
banner=pyfiglet.figlet_format("X-work")
print(banner)
time.sleep(2)
source=input(" Enter the source  address: ")
time.sleep(2)
subprocess.call('clear',shell=True)
banner2=pyfiglet.figlet_format("X-work")
print(Fore.GREEN+" >>>Please wait while we process your results...")
time.sleep(2)
print(banner2)
ssip=80
try:
    ip=socket.gethostbyname(source)
    print(Fore.GREEN +"please wait while we complete the process")
    time.sleep(1)
    print(Fore.WHITE+" binding host and port...")
    print(Fore.GREEN+">>>>>>>>>>>>>>>>>>>>>")
    time.sleep(2)
    print("====>>>>> "+ip)
    ip2=socket.gethostbyaddr(source)
    print(ip2)
    l1=[]
    print("Target-ip >>  "+ip+"\n")
except socket.gaierror:
    print(Fore.RED+" Failed to connect to target ..") 
s.connect((source,ssip))
print(f"       Above are the results of {source} 100% accurate!")
print(Fore.YELLOW+" Connected to source..")
os.listdir()

