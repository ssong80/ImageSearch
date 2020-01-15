import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import PyQt5

from tensorflow.contrib.learn.python.learn.datasets.mnist import extract_images, extract_labels

import numpy as np

UI_Name = "App.ui"

form_class = uic.loadUiType(UI_Name)[0]

_image_data = 0
_train_images = 0
_train_labels = 0
_test_images = 0
_test_labels = 0
_learning_rate = 0
_batch_size = 0
_num_epoch = 0
validation_size = 5000

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_LoadImage.clicked.connect(self.buttonFunction)
        self.pushButton_LoadTrainImageData.clicked.connect(self.loadTrainImageData_buttonFunction)
        self.pushButton_LoadTrainLabelData.clicked.connect(self.loadTrainLabelData_buttonFunction)
        self.pushButton_LoadTestImageData.clicked.connect(self.loadTestImageData_buttonFunction)
        self.pushButton_LoadTestLabelData.clicked.connect(self.loadTestLabelData_buttonFunction)
        self.pushButton_Train.clicked.connect(self.Train_buttonFunction)

        self.lineEdit_LearningRate.textChanged.connect(self.inputLearningRate_textFunction)
        self.lineEdit_BatchSize.textChanged.connect(self.inputBatchSize_textFunction)
        self.lineEdit_Epoch.textChanged.connect(self.inputEpoch_textFunction)

        self.image_data = _image_data
        self.train_images = _train_images
        self.train_labels = _train_labels
        self.test_images = _test_images
        self.test_labels = _test_labels
        self.learning_rate = _learning_rate
        self.batch_size = _batch_size
        self.num_epoch = _num_epoch

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

    def loadTrainImageData_buttonFunction(self):
        f_path = QFileDialog.getOpenFileName(self)
        path = f_path[0]
        print(path)
        with open(path, 'rb') as f:
            train_images = extract_images(f)
        TRAINING_SIZE = len(train_images)
        print(TRAINING_SIZE)

    def loadTrainLabelData_buttonFunction(self):
        f_path = QFileDialog.getOpenFileName(self)
        path = f_path[0]
        print(path)
        with open(path, 'rb') as f:
            train_labels = extract_labels(f)
        

    def loadTestImageData_buttonFunction(self):
        f_path = QFileDialog.getOpenFileName(self)
        path = f_path[0]
        print(path)
        with open(path, 'rb') as f:
            test_images = extract_images(f)
        TEST_SIZE = len(test_images)
        print(TEST_SIZE)

    def loadTestLabelData_buttonFunction(self):
        f_path = QFileDialog.getOpenFileName(self)
        path = f_path[0]
        print(path)
        with open(path, 'rb') as f:
            test_labels = extract_labels(f)

    def inputLearningRate_textFunction(self):
        learning_rate = self.lineEdit_LearningRate.text()
        print(learning_rate)

    def inputBatchSize_textFunction(self):
        batch_size = self.lineEdit_BatchSize.text()
        print(batch_size)

    def inputEpoch_textFunction(self):
        num_epoch = self.lineEdit_Epoch.text()
        print(epoch)

    def Train_buttonFunction(self):        
        learning_rate = self.lineEdit_LearningRate.text()
        print('learning rate : {0}'.format(learning_rate))
        batch_size = self.lineEdit_BatchSize.text()
        print('batch size : {0}'.format(batch_size))
        num_epoch = self.lineEdit_Epoch.text()
        print('epoch : {0}'.format(num_epoch))

        image_validation = train_images[-validation_size:]
        image_train = train_images[:validation_size]   






if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    