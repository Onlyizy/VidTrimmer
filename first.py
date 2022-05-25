import cv2
import numpy as np
import os
from datetime import datetime

log=open("log.txt","a")
time=datetime.now

log.writelines(datetime)

video=cv2.VideoCapture("")

print(log.read())

log.close()
