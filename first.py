import cv2
import numpy as np
import os
from datetime import datetime

VID_FILETYPES=[".mp4",".mov",".avi",".flv",".mkv",".wmv","h264",".264","mpeg"]

def finder()->bool:
  log=open("log.txt","a")
  time=datetime.now
  log.write(datetime)
  path=input("Copy the path to the directory and paste it here: ")
  lsdir=os.list.dir(path)
  log.write(path)
  log.writelines(lsdir)
  for file in lsdir:
    if file[::-1][:-3][::-1].lower() in VID_FILETYPES:
      
      
  

def trimmer()->bool:
  


def logwriter()->bool:
  






  video=cv2.VideoCapture("")

  print(log.read())

  log.close()


if __name__==__main__:
