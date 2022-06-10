#import cv2
import numpy as np
import os
from datetime import datetime
from moviepy.editor import *

#This script requires the moviepy package and may require cv2 in future updates. 

VID_FILETYPES=[".mp4",".mov",".avi",".flv",".mkv",".wmv","h264",".264","mpeg"]

def findandTrim(path:str,timeset:int)->int:
  counter=0
  cuttracker={}
  lsdir=os.listdir(path)
  for file in lsdir:
    clipcount=0
    for ext in VID_FILETYPES:
      newclips=[]
      if file.lower().endswith(ext):
        video=VideoFileClip(path+"\\"+file)
        duration=float(video.duration)
        if duration>timeset:
          for start in range(int(duration))[::timeset]:
            if start+timeset<=duration:
              newclips.append(video.subclip(start,start+timeset))
            else:
              newclips.append(video.subclip(start,))
          for newclip in newclips:
            newclip.write_videofile(str(clipcount)+file)
            clipcount+=1
          cuttracker.setdefault(file,clipcount)
        counter+=1
  logwriter(path,counter,cuttracker)
  return counter

def usrprompt():
  while True:
    path=input("Copy the path to the directory and paste it here: ")
    timeset=int(input("Please enter the number of seconds you would like the videos to be trimmed to. We recommend either 30s or 10s for social media content: "))
    findandTrim(path,timeset)
  
def logwriter(path:str,counter,cuttracker)->bool:
  log=open("log.txt","a+")
  log.write(str(datetime.now()))
  log.write("\n")
  lsdir=os.listdir(path)
  log.write("PATH: " + path)
  log.write("\n")
  log.write("FILES IN DIRECTORY: ")
  log.writelines(lsdir)
  log.write("\n")
  log.write(counter+" videos processed")
  log.write("\n")
  for video in cuttracker.keys():
    log.write(video+" was trimmed into "+cuttracker[video]+"clips")
  log.write("="*100)
  print(log.read())
  log.close()

if __name__=="__main__":
  usrprompt()
