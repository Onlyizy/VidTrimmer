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
  print(lsdir)
  for file in lsdir:
    for ext in VID_FILETYPES:
      if file.endswith(ext):
        print()
        print(file)
        clipcount=0
        video=VideoFileClip(path+"\\"+file)
        duration=float(video.duration)
        if duration>timeset:
          for start in range(int(duration))[::timeset]:
            print("start=",start)
            print()
            print("duration=",duration)
            print()
            print("timeset=",timeset)
            newclips.append(video.subclip(start,start+timeset))
            clipcount=+1
            print(newclips)
          for newclip in newclips:
            print(newclip)
            print("clipcount=",clipcount)
            newclip.write_videofile(str(clipcount)+file)
            print("done")
          cuttracker.setdefault(file,clipcount)
          print("done")
        counter=+1
  logwriter(path,counter,cuttracker)
  print("done")
  return counter

def usrprompt():
  while True:
    path=input("Copy the path to the directory and paste it here: ")
    timeset=int(input("Please enter the number of seconds you would like the videos to be trimmed to. We recommend either 30s or 10s for social media content: "))
    findandTrim(path,timeset)
  
def logwriter(path:str,counter,cuttracker)->bool:
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

