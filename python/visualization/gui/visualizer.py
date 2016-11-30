from PyQt4 import QtCore, QtGui
from mainWindow import Ui_MainWindow
from drawer import Drawer
from load_csv import load_csv
from trackingDataHandler import DataHandler
import numpy as np
import time
import cv2


from analyses.example_egoMotion.egoMotionPlot import EgoMotionPlot
from analyses.example_swarm.swarmPlot import SwarmPlot




class Visualizer(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.play_type_dict = {"Video":0, "Draw":1}
        self.play_type = self.play_type_dict["Draw"]


        self.ui.actionLoadVideo.triggered.connect(self.load_video)
        self.ui.actionLoadCsv.triggered.connect(self.load_csv)
        self.ui.actionLoadAnalyseResult.triggered.connect(self.load_analyse_result)

        self.frame_id=0



        # player
        self.ui.frameID.setText(str(self.frame_id))
        self.play_timer = Timer()
        self.played = False
        self.ui.playBtn.setText('play')


        self.stepPlaySize = 1

        # plot & analyse
        self.fish_id = 1
        self.show_plot = False

        string_list = ['None', 'swarm_anlysis', 'ego_motion']
        self.ui.analyseComboBox.addItems(string_list)

        self.anaylse_canvas = None

        self.l = QtGui.QVBoxLayout(self.ui.widget)
        self.anaylse_layout = QtGui.QVBoxLayout(self.ui.analyse_widget)
        self.fish_list_combo = None


        self.connect(self.ui.showPlotBtn, QtCore.SIGNAL("clicked()"), self.showPlot)
        self.connect(self.ui.sptBtn, QtCore.SIGNAL("clicked()"), self.switchPlayType)
        self.connect(self.ui.playBtn, QtCore.SIGNAL("clicked()"), self.videoPlayPause)
        self.connect(self.ui.stepSize, QtCore.SIGNAL('valueChanged(int)'), self.changeStepSize)
        self.connect(self.play_timer, QtCore.SIGNAL('updatePlay()'), self.playVideo)
        self.connect(self.ui.nextBtn, QtCore.SIGNAL('clicked()'), self.playNextFrame)
        self.connect(self.ui.backBtn, QtCore.SIGNAL('clicked()'), self.playLastFrame)
        self.connect(self.ui.playerSlider, QtCore.SIGNAL('silderPressed()'), self.pauseVideo)
        self.connect(self.ui.playerSlider, QtCore.SIGNAL('sliderMoved(int)'), self.playFrame)
        self.connect(self.ui.playerSlider, QtCore.SIGNAL('sliderReleased()'), self.pauseVideo)
        self.connect(self.ui.changeColorBtn, QtCore.SIGNAL("clicked()"), self.changeFishColor)
        self.connect(self.ui.fishList, QtCore.SIGNAL("itemSelectionChanged()"), self.showColor)
        self.connect(self.ui.analyseComboBox, QtCore.SIGNAL("currentIndexChanged(int) "), self.changeAnalysis)




    @QtCore.pyqtSlot()
    def showPlot(self):
        if self.show_plot == False:
            self.show_plot = True
            self.ui.showPlotBtn.setText('True')
        else:
            self.show_plot = False
            self.ui.showPlotBtn.setText('False')

            for i in reversed(range(self.l.count())):
                self.l.itemAt(i).widget().setParent(None)


    @QtCore.pyqtSlot(int)
    def changeAnalysis(self,id):
        if str(self.ui.analyseComboBox.currentText()) == 'swarm_anlysis':
            self.anaylse_canvas = SwarmPlot(self.anaylse_result_filename, self.frame_begin_ID)
            for i in reversed(range(self.l.count())):
                self.l.itemAt(i).widget().setParent(None)
            for i in reversed(range(self.anaylse_layout.count())):
                self.anaylse_layout.itemAt(i).widget().setParent(None)

            if self.show_plot == True:
                self.l.addWidget(self.anaylse_canvas)

        elif str(self.ui.analyseComboBox.currentText()) == 'ego_motion':
            self.anaylse_canvas = EgoMotionPlot(self.anaylse_result_filename, self.frame_begin_ID)
            for i in reversed(range(self.l.count())):
                self.l.itemAt(i).widget().setParent(None)
            for i in reversed(range(self.anaylse_layout.count())):
                self.anaylse_layout.itemAt(i).widget().setParent(None)

            if self.show_plot == True:
                self.l.addWidget(self.anaylse_canvas)
                fish_list = []
                self.fish_list_combo = QtGui.QComboBox()
                self.fish_list_combo.clear()
                for i in range(self.dat_handler.fish_Num):
                    fish_list.append('Fish_' + str(i + 1))
                self.fish_list_combo.addItems(fish_list)
                self.anaylse_layout.addWidget(self.fish_list_combo)

        elif str(self.ui.analyseComboBox.currentText()) == 'None':
            for i in reversed(range(self.l.count())):
                self.l.itemAt(i).widget().setParent(None)
            for i in reversed(range(self.anaylse_layout.count())):
                self.anaylse_layout.itemAt(i).widget().setParent(None)


    def load_video(self):
        name = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        self.cap = cv2.VideoCapture(name)



    def load_csv(self):
        name = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))
        self.dat_handler = DataHandler(load_csv(name))
        self.frame_begin_ID = self.dat_handler.get_begin_ID()
        self.frame_end_ID = self.dat_handler.get_end_ID()
        self.frame_id = self.frame_begin_ID
        self.color_dict = {}
        fishString = QtCore.QStringList()
        for i in range(self.dat_handler.fish_Num):
            self.color_dict[i + 1] = (0, 0, 0)
            fishString.append('Fish_' + str(i + 1))

        self.ui.fishList.addItems(fishString)

        self.ui.playerSlider.setMinimum(self.frame_begin_ID)
        self.ui.playerSlider.setMaximum(self.frame_end_ID)


    def load_analyse_result(self):
        self.anaylse_result_filename = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File'))

    @QtCore.pyqtSlot()
    def changeFishColor(self):
        color_dia = QtGui.QColorDialog()
        color = QtGui.QColor(color_dia.getColor())
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, color)
        self.ui.label_test.setPalette(pe)
        self.ui.fishList.currentItem().setForeground(color)
        self.color_dict[self.ui.fishList.currentRow()+1] = (color.getRgb())[:-1]

    @QtCore.pyqtSlot()
    def showColor(self):
        color = self.color_dict[self.ui.fishList.currentRow()+1]
        qcolor = QtGui.QColor.fromRgb(color[0], color[1], color[2], 255)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, qcolor)
        self.ui.label_test.setPalette(pe)

    @QtCore.pyqtSlot(int)
    def switchPlayType(self):
        if self.play_type == self.play_type_dict["Video"]:
            self.play_type = self.play_type_dict["Draw"]
            self.ui.drawTabWidget.show()
        else:
            self.play_type = self.play_type_dict["Video"]
            self.ui.drawTabWidget.hide()


    @QtCore.pyqtSlot(int)
    def changeStepSize(self, step):
        self.stepPlaySize = step


    @QtCore.pyqtSlot()
    def pauseVideo(self):
        self.played = False
        self.ui.playBtn.setText('play')
        self.play_timer.stop()


    @QtCore.pyqtSlot()
    def videoPlayPause(self):
        if self.played == False:
            self.played = True
            self.ui.playBtn.setText('pause')
            self.play_timer.start()
        else:
            self.played = False
            self.ui.playBtn.setText('play')
            self.play_timer.stop()


    def drawFrame(self):
        if self.play_type == self.play_type_dict["Video"]:
            self.cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, self.frame_id)
            ret, frame = self.cap.read()

        else:
            screen = np.zeros((400,400,3), np.uint8)
            drawer = Drawer(screen, 400, 400, self.color_dict)

            if self.ui.showID_CheckBox.isChecked():
                drawer.showId(True)
            else:
                drawer.showId(False)

            drawer.set_draw_form(str(self.ui.fishFormComboBox.currentText()))
            drawer.set_tracker_version(str(self.ui.trackerVersion.currentText()))

            frame = drawer.draw(self.dat_handler.get_frame_dat(self.frame_id))


        self.ui.frameID.setText(str(self.frame_id))

        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap(image)
        myScaledPixmap = pix.scaled(self.ui.showVideo.size())
        self.ui.showVideo.setPixmap(myScaledPixmap)


        if self.anaylse_canvas != None and self.show_plot == True:
            if not (self.fish_list_combo is None):
                self.fish_id = self.fish_list_combo.currentIndex()+1
            self.anaylse_canvas.showPlot(self.frame_id, self.fish_id)
            self.play_timer.set_sleep_time(0.9)
        else:
            self.play_timer.set_sleep_time(0.05)


    @QtCore.pyqtSlot()
    def playVideo(self):
        self.drawFrame()
        self.ui.playerSlider.setValue(self.frame_id)
        if self.frame_id < self.frame_end_ID:
            self.frame_id = self.frame_id+1



    @QtCore.pyqtSlot()
    def playNextFrame(self):

        self.pauseVideo()

        self.frame_id = self.frame_id + self.stepPlaySize
        if self.frame_id > self.frame_end_ID:
            self.frame_id = self.frame_end_ID


        self.ui.playerSlider.setValue(self.frame_id)
        self.drawFrame()

    @QtCore.pyqtSlot()
    def playLastFrame(self):

        self.pauseVideo()

        self.frame_id = self.frame_id - self.stepPlaySize

        if self.frame_id < self.frame_begin_ID:
            self.frame_id = self.frame_begin_ID


        self.ui.playerSlider.setValue(self.frame_id)
        self.drawFrame()

    @QtCore.pyqtSlot()
    def playFrame(self, value):

        self.pauseVideo()
        self.frame_id = self.ui.playerSlider.value()
        self.ui.frameID.setText(str(self.frame_id))

        self.drawFrame()




class Timer(QtCore.QThread):
    def __init__(self, signal = "updatePlay()", parent=None):
        super(Timer, self).__init__(parent)
        self.stoped = False
        self.signal = signal
        self.mutex = QtCore.QMutex()

        self.sleep_time = 0.05

    def set_sleep_time(self,sleep_time):
        self.sleep_time = sleep_time

    def run(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stoped = False
        while True:
            if self.stoped:
                return


            self.emit(QtCore.SIGNAL(self.signal))

            # set fps
            time.sleep( self.sleep_time )

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stoped = True

    def isStoped(self):
        with QtCore.QMutexLocker(self.mutex):
            return self.stoped






