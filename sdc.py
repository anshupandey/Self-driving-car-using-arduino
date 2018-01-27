import os
import sys
import serial
from PyQt5 import QtGui
from PyQt5 import QtCore,QtWidgets
from skimage import io
global url,fnum,bnum,rnum,lnum,snum
fnum=0
snum=0
bnum=0
rnum=0
lnum=0

class window(QtWidgets.QMainWindow):
   def __init__(self):
      super(window,self).__init__()
      self.setGeometry(50,50,1400,900)
      self.setWindowTitle("Self Driving Car App | www.techtrunk.in")
      self.setWindowIcon(QtGui.QIcon('icon.png'))
      self.label1=QtWidgets.QLabel("COM Port(e.g. COM13)",self)
      self.label1.resize(200,30)
      self.label1.move(50,80)
      self.comport=QtWidgets.QLineEdit(self)
      self.comport.move(50,115)
      self.comport.resize(80,30)
      self.cameraurl=QtWidgets.QLineEdit(self)
      self.cameraurl.move(50,220)
      self.cameraurl.resize(200,30)
      self.label2=QtWidgets.QLabel("URL",self)
      self.label2.resize(100,50)
      self.label2.move(50,180)
      self.label3=QtWidgets.QLabel("e.g. http://192.168.1.6:8080/shot.jpg",self)
      self.label3.resize(500,50)
      self.label3.move(50,250)
      self.fwd=QtWidgets.QPushButton("Forward",self)
      self.fwd.resize(80,50)
      self.fwd.move(130,320)
      self.lft=QtWidgets.QPushButton("Left",self)
      self.lft.resize(80,50)
      self.lft.move(30,400)
      self.rgt=QtWidgets.QPushButton("Right",self)
      self.rgt.resize(80,50)
      self.rgt.move(230,400)
      self.bck=QtWidgets.QPushButton("Backward",self)
      self.bck.resize(80,50)
      self.bck.move(130,480)
      self.stp=QtWidgets.QPushButton("Stop",self)
      self.stp.resize(80,50)
      self.stp.move(130,400)
      self.fwd.clicked.connect(self.forward)
      self.start=QtWidgets.QPushButton("Start",self)
      self.start.resize(80,50)
      self.start.move(80,600)
      self.stop=QtWidgets.QPushButton("Close",self)
      self.stop.resize(80,50)
      self.stop.move(180,600)
      self.start.clicked.connect(self.openport)
      self.stop.clicked.connect(self.closeport)
      self.image=QtWidgets.QLabel(self)
      self.image.resize(1000,500)
      self.image.move(320,100)
      self.image2=QtWidgets.QLabel(self)
      self.image2.resize(500,90)
      self.image2.move(20,750)
      self.image2.setPixmap(QtGui.QPixmap(r'logo.jpg'))
      self.direction=QtWidgets.QLabel("direction",self)
      self.direction.resize(100,50)
      self.direction.move(800,600)
      self.lft.clicked.connect(self.left)
      self.rgt.clicked.connect(self.right)
      self.bck.clicked.connect(self.backward)
      self.stp.clicked.connect(self.stopdir)           
      self.show()

   def openport(self):
      com=self.comport.text()
      self.url=self.cameraurl.text()      
      self.s=serial.Serial(com,9600)

   def closeport(self):
      self.s.close()


   def forward(self):
      global fnum
      self.s.write(b'f')
      img=io.imread(self.url)
      io.imsave(r'C:\python35\testsdc\forward_'+str(fnum)+".jpg",img)
      self.image.setPixmap(QtGui.QPixmap(r'C:\python35\testsdc\forward_'+str(fnum)+".jpg"))
      fnum=fnum+1
      self.direction.setText("Forward")


   def right(self):
      global rnum
      self.s.write(b'r')
      img=io.imread(self.url)
      io.imsave(r'C:\python35\testsdc\right_'+str(rnum)+".jpg",img)
      self.image.setPixmap(QtGui.QPixmap(r'C:\python35\testsdc\right_'+str(rnum)+".jpg"))
      rnum=rnum+1
      self.direction.setText("Right")

   def left(self):
      global lnum
      self.s.write(b'l')
      img=io.imread(self.url)
      io.imsave(r'C:\python35\testsdc\left_'+str(lnum)+".jpg",img)
      self.image.setPixmap(QtGui.QPixmap(r'C:\python35\testsdc\left_'+str(lnum)+".jpg"))
      lnum=lnum+1
      self.direction.setText("Left")

   def backward(self):
      global bnum
      self.s.write(b'b')
      img=io.imread(self.url)
      io.imsave(r'C:\python35\testsdc\backward_'+str(bnum)+".jpg",img)
      self.image.setPixmap(QtGui.QPixmap(r"C:\python35\testsdc\backward_"+str(bnum)+".jpg"))
      bnum=bnum+1
      self.direction.setText("Backward")

   def stopdir(self):
      global snum
      self.s.write(b's')
      img=io.imread(self.url)
      io.imsave(r'C:\python35\testsdc\stop_'+str(snum)+".jpg",img)
      self.image.setPixmap(QtGui.QPixmap(r'C:\python35\testsdc\stop_'+str(snum)+".jpg"))
      snum=snum+1
      self.direction.setText("Stop")
      
app=QtWidgets.QApplication(sys.argv)
GUI=window()
sys.exit(app.exec_())
