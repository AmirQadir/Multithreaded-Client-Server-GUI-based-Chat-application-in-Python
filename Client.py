#from socket import AF_INET, socket, SOCK_STREAM
import socket
import threading
from ClientUI import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import time


import PyQt5
import sys

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
 
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)




def ReceiveMsg():
	while(True):
		if(ok==True):
			msg = s.recv(1024)
			decoded = msg.decode('ascii')
			print("S:",decoded)
			ui.textBrowser.append("S: " + decoded)
			if(decoded=="E"):
				s.close()
				break

# def SendMsg():
# 	while(True):
# 		msg = input()
# 		s.send(msg.encode('ascii'))
# 		if(msg=="E"):
# 			s.close()
# 			break

def SendMsg():
	# while(True):
	#msg = input()
	msg = ui.textEdit.toPlainText()
	ui.textEdit.clear()
	s.send(msg.encode('ascii'))
	ui.textBrowser.append("C: " + msg)
	if(msg=="E"):
		s.close()
		#break

def connectFunc():
	ip = ui.textEdit_2.toPlainText()
	port = ui.textEdit_3.toPlainText()

	#host = socket.gethostname()
	#port = 27035
	addr = (ip, int(port))
	s.connect(addr)
	global ok
	ok = True


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting " + self.name)
        if(self.threadID==1):
            ReceiveMsg()
        else:
            #SendMsg()
            pass



#KIVY

if __name__ == "__main__":
	import sys
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ok = False
	# Create new threads
	thread1 = myThread(1, "Thread-1")
	thread2 = myThread(2, "Thread-1")
	# Start new Threads
	thread1.start()
	thread2.start()

	

	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	ui.pushButton_2.clicked.connect(connectFunc)	
	ui.pushButton.clicked.connect(SendMsg)
	Dialog.show()
	id = app.exec_()

	
	#s.connect(ADDR)


	
