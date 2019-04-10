#from socket import AF_INET, socket, SOCK_STREAM
import socket
import threading
from ServerUI import Ui_Dialog
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
			msg = clientsocket.recv(1024)
			decoded = msg.decode('ascii')
			print("C:",decoded)
			ui.textBrowser.append("C: " + decoded)
			if(decoded=="E"):
				clientsocket.close()
				break

def SendMsg():
	# while(True):
	#msg = input()
	msg = ui.textEdit.toPlainText()
	ui.textEdit.clear()
	clientsocket.send(msg.encode('ascii'))
	ui.textBrowser.append("S: " + msg)
	if(msg=="E"):
		clientsocket.close()
		#break

def connectFunc():
	port = ui.textEdit_2.toPlainText()

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	host = socket.gethostname()
	
	ADDR = (host, int(port))

	#s.connect(ADDR)

	serversocket.bind(ADDR)


	serversocket.listen(5)

	global clientsocket
	clientsocket, address = serversocket.accept()

	print("Got a connection From %s "%str(address))
	global ok
	ok = True


	
class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        #print ("Starting " + self.name)
        if(self.threadID==1):
            ReceiveMsg()
        else:
        	pass
            # SendMsg()
            # buttonChecker()




if __name__ == "__main__":
	import sys
	clientsocket = None
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


	


	
	



	# sys.exit(id)
