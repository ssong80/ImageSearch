import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import PyQt5

UI_Name = "App.ui"

form_class = uic.loadUiType(UI_Name)[0]

_image_data = 0

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_OpenFolder.clicked.connect(self.buttonFunction)
        self.image_data = _image_data

    def buttonFunction(self):
        f_path = QFileDialog.getOpenFileName(self)
        global file_path
        file_path = f_path
        image_data = QImage()
        image_data.load(f_path[0])
        image = QPixmap()
        image = QPixmap.fromImage(image_data)

        image = image.scaledToWidth(200)
        image = image.scaledToHeight(200)

        scene = QGraphicsScene()
        scene.addPixmap(image)
        self.graphicsView_LoadImage.setScene(scene)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    