import sys
import os
import pathlib
from platform import platform
import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QStackedWidget, QFileDialog
import pygame #pip install pygame
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from sqlalchemy import true
import Ui_sk8_system_pages
import shutil

class  StackedWidget:
    def __init__(self):
        super().__init__()
        self.main_win = QStackedWidget()
        self.ui = Ui_sk8_system_pages.Ui_StackedWidget()
        self.ui.setupUi(self.main_win)
        self.main_win.setCurrentIndex(0)
        self.isVideoChangedLoading=False
        self.isVideoChangedSke=False
        self.filename=''
        self.ui.btn1.clicked.connect(self.btn1_func)
        self.ui.btn2.clicked.connect(self.btn2_func)
        self.ui.btn3.clicked.connect(self.btn3_func)
        self.ui.btn4.clicked.connect(self.home_func)
        self.ui.btn5.clicked.connect(self.home_func)
        self.ui.btn6.clicked.connect(self.home_func)
        self.ui.audio_btn.clicked.connect(self.audio_btn_func)
        
        self.ui.upload_btn.clicked.connect(self.open_file)
        self.ui.player = QMediaPlayer()
        self.ui.player.setVideoOutput(self.ui.vid_wget)        
        self.ui.play_btn.clicked.connect(self.play_btn_func)
        self.ui.stop_btn.clicked.connect(self.stop_btn_func)
        self.ui.pause_btn.clicked.connect(self.pause_btn_func)
        
        self.ui.analysis_btn.clicked.connect(self.analysis_btn_func)
        self.ui.player.mediaStatusChanged.connect(self.statusChanged)
        self.ui.save_btn.clicked.connect(self.saveToFile)


    def btn1_func(self):
        self.main_win.setCurrentIndex(1)
    def btn2_func(self):
        self.main_win.setCurrentIndex(2)
    def btn3_func(self):
        self.main_win.setCurrentIndex(3)
    def home_func(self):
        self.main_win.setCurrentIndex(0)
    
    def saveToFile(self):
        if(self.filename[-5] == 'A'):
            shutil.copy2('./accuracy video/19_M_1_1_3A_acc.mp4', './result/Axel/19_M_1_1_3A_result.mp4')
        elif(self.filename[-5] == 'z'):
            shutil.copy2('./accuracy video/19_M_11_8_3Lz_acc.mp4', './result/Lutz/19_M_11_8_3Lz_result.mp4')
        elif(self.filename[-5] == 'T'):
            shutil.copy2('./accuracy video/19_M_21_2_4T_acc.mp4', './result/Toeloop/19_M_21_2_4T_result.mp4')

    def audio_btn_func(self):
        
        pygame.init()
        
        if(self.filename[-5] == 'A'):
            sound = pygame.mixer.Sound(os.getcwd()+"\\Audio_Guide\\3A_audio.mp3")
        elif(self.filename[-5] == 'z'):
            sound = pygame.mixer.Sound(os.getcwd()+"\\Audio_Guide\\3Lz_audio.mp3")
        elif(self.filename[-5] == 'T'):
            sound = pygame.mixer.Sound(os.getcwd()+"\\Audio_Guide\\4T_audio.mp3")
        
        if pygame.mixer.get_busy() == 1:
            pygame.mixer.pause()
        sound.set_volume(1)
        sound.play()
        
    def open_file(self):
        self.filename = QFileDialog.getOpenFileUrl()[0]
        self.ui.player.setMedia(QMediaContent(self.filename)) 
        print(self.filename)
        if str(self.filename).split('.')[2]!="QUrl('')":
            self.filename = str(self.filename).split('/')[11].split('\'')[0]  #所選取的檔名
            print(self.filename)

    def statusChanged(self, status):
        if status==QMediaPlayer.EndOfMedia:
            if not self.isVideoChangedSke and not self.isVideoChangedLoading:
                self.ui.player.play()
            elif (self.filename[-5] == 'A') and self.isVideoChangedLoading:
                self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/skeleton video/19_M_1_1_3A_ske0.5.avi'))) #放骨架的路徑
                self.ui.player.play()
                self.isVideoChangedSke=True
                self.isVideoChangedLoading=False
            elif (self.filename[-5] == 'z') and self.isVideoChangedLoading:
                self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/skeleton video/19_M_11_8_3Lz_ske0.5.avi'))) #放骨架的路徑
                self.ui.player.play()
                self.isVideoChangedSke=True
                self.isVideoChangedLoading=False
            elif (self.filename[-5] == 'T') and self.isVideoChangedLoading:
                self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/skeleton video/19_M_21_2_4T_ske0.5.avi'))) #放骨架的路徑
                self.ui.player.play()
                self.isVideoChangedSke=True
                self.isVideoChangedLoading=False
            elif(self.filename[-5] == 'A') and self.isVideoChangedSke:
                self.ui.jump_name.setText("Axel")
                self.ui.num_of_turns.setText("3.5")
                self.ui.mistake_bool.setText("No")
                self.ui.take_off_foot.setText("Left foot")
                self.ui.take_off_edge.setText("Outside edge")
                self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/accuracy video/19_M_1_1_3A_acc.mp4')))
                self.ui.player.play()
                self.isVideoChangedSke=False
            elif(self.filename[-5] == 'z') and self.isVideoChangedSke:
                self.ui.jump_name.setText("Lutz")
                self.ui.num_of_turns.setText("3")
                self.ui.mistake_bool.setText("No")
                self.ui.take_off_foot.setText("Left foot")
                self.ui.take_off_edge.setText("Outside edge")
                self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/accuracy video/19_M_11_8_3Lz_acc.mp4')))
                self.ui.player.play()
                self.isVideoChangedSke=False
            elif(self.filename[-5] == 'T') and self.isVideoChangedSke:
                self.ui.jump_name.setText("Toeloop")
                self.ui.num_of_turns.setText("4")
                self.ui.mistake_bool.setText("No")
                self.ui.take_off_foot.setText("Right foot")
                self.ui.take_off_edge.setText("Outside edge")
                self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/accuracy video/19_M_21_2_4T_acc.mp4')))
                self.ui.player.play()
                self.isVideoChangedSke=False
                

    def play_btn_func(self):
        self.ui.player.play()
    
        
    def stop_btn_func(self):        
        self.ui.player.stop()
        self.ui.jump_name.setText("")
        self.ui.num_of_turns.setText("")
        self.ui.mistake_bool.setText("")
        self.ui.take_off_foot.setText("")
        self.ui.take_off_edge.setText("")
        
    def pause_btn_func(self):       
        self.ui.player.pause()
        self.playflag=False
        
    def analysis_btn_func(self):
        
        if(self.filename[-5] == 'A'):
            self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/loading.mp4' ))) #放loading的路徑
            self.isVideoChangedLoading=True
            self.ui.player.play()
        elif(self.filename[-5] == 'z'):
            self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/loading.mp4' ))) #放loading的路徑
            self.isVideoChangedLoading=True
            self.ui.player.play()
            
        elif(self.filename[-5] == 'T'):
            self.ui.player.setMedia(QMediaContent(PyQt5.QtCore.QUrl('file:///C:/Users/user/Desktop/專題/專題成果展/sk8_system/loading.mp4' ))) #放loading的路徑
            self.isVideoChangedLoading=True
            self.ui.player.play()
            
        
        
    def show(self):
        self.main_win.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = StackedWidget()
    main_win.show()
    sys.exit(app.exec_())
    
    
    