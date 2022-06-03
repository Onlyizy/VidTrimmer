import cv2
import numpy as np
import os
from datetime import datetime
from moviepy.editor import *

#This script requires multiple dependencies and requires you to 

VID_FILETYPES=[".mp4",".mov",".avi",".flv",".mkv",".wmv","h264",".264","mpeg"]

def finder(path:str,timeset:int)->int:
  counter=0
  lsdir=os.listdir(path)
  #for file in lsdir:
    #if file[::-1][:-3][::-1].lower() in VID_FILETYPES:
      #check if file is more than timeset seconds
      #if  time_of_video<=timeset:
        #pass
      #else:
        #trim
        #counter+=1
  logwriter(path)
  return counter

def usrprompt()->tuple:
  while True:
    path=input("Copy the path to the directory and paste it here: ")
    timeset=int(input("Please enter the number of seconds you would like the videos to be trimmed to. We recommend either 30s or 10s for social media content: "))
    finder(path,timeset)
  

def trimmer()->bool:
  video=cv2.VideoCapture("")
  


def logwriter(path:str)->bool:
  log=open("log.txt","a+")
  time=datetime.now()
  log.write(str(time))
  log.write("\n")
  lsdir=os.listdir(path)
  log.write(path)
  log.write("\n")
  log.writelines(lsdir)
  print(log.read())
  log.close()

if __name__=="__main__":
  usrprompt()

