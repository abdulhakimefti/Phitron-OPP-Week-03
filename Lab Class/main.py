"""
My camera application
author: Abdul Hakim
"""
# now install GUI library
# pip install pyqt5
 

import sys  
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage,QIcon
import cv2

class Window(QWidget):
    """Main app window"""
    def __init__(self):
        super.__init__()
    #variable for app window
        self.window_width= 640
        self.window_height = 400
    #image variable
        self.image_width= 640
        self.image_height = 400
    #setup the window 
        self.setWindowTitle("My Camera App")
        self.setFixedSize(self.window_width,self.window_height)
        self.ui()
        
    def ui(self):
        """update all ui things"""
        self.image_label= QLabel(self)
        self.image_label.setGeometry(0,0,self.image_width,self.image_height)
        self.show()
    
    def update(self):
        """update forms"""
        pass
    
    def save_img(self):
        """save image from camera"""
        pass
    
    def record(self):
        """save record video"""
        pass

#app run
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())