import cv2
import numpy as np
import os
from datetime import datetime
from moviepy.editor import *

#This script requires multiple dependencies and requires you to 

VID_FILETYPES=[".mp4",".mov",".avi",".flv",".mkv",".wmv","h264",".264","mpeg"]

def findandTrim(path:str,timeset:int)->int:
  counter=0
  newclips=[]
  cuttracker={}
  lsdir=os.listdir(path)
  for file in lsdir:
    if file[::-1][:-3][::-1].lower() in VID_FILETYPES:
      clipcount=0
      video=VideoFileClip(file)
      duration=float(clip.duration)
      if duration>timeset:
        for start in range(duration.ceil())[::timeset]:
          newclips.append(video.subclip(start,start+timeset))
          clipcount=+1
        cuttracker.setdefault(file,clipcount)
     counter=+1
  logwriter(path,counter,cuttracker)
  return counter

def usrprompt():
  while True:
    path=input("Copy the path to the directory and paste it here: ")
    timeset=int(input("Please enter the number of seconds you would like the videos to be trimmed to. We recommend either 30s or 10s for social media content: "))
    finder(path,timeset)
  
def logwriter(path:str,)->bool:
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

