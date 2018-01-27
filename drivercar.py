from skimage import io
from sklearn.externals import joblib
import os
import sys
import time
import serial
global url
import numpy
import cv2
url="http://192.168.43.1:8080/shot.jpg"
s=serial.Serial('COM10',9600)
time.sleep(2)

alg=joblib.load('mymodel.mkl')
#scaler=joblib.load('scalermodel.pkl')
print('model loaded')

def drive():
    img=io.imread(url)
    cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=cv2.blur(img,(5,5))
    retval,img=cv2.threshold(img,210,255,cv2.THRESH_BINARY)
    img=cv2.resize(img,(24,24))
    retval,img=cv2.threshold(img,210,255,cv2.THRESH_BINARY)
    image_as_array=numpy.ndarray.flatten(numpy.array(img))
    #image_as_array=scaler.transform(image_as_array)
    result=alg.predict([image_as_array])[0]
    if result=='forward':
        s.write(b'f')
        time.sleep(1)
    elif result=='right':
        s.write(b'r')
        time.sleep(1)
    elif result=='left':
        s.write(b'l')
        time.sleep(1)
    time.sleep(1)
    print(result)
    drive()
print("Start Driving")
drive()
s.close()