# from analyses.BaseAnlysisPlot import *
import scipy.io
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class EgoMotionPlot(FigureCanvas):
    def __init__(self, file, frame_begin):
        # self.file = file
        self.fish_id = 1
        print file

        self.fig = plt.figure()

        FigureCanvas.__init__(self, self.fig)


        self.data = self.__load_data(file)
        self.frame_begin = frame_begin

        # self.showPlot(1000, 1)

    def __load_data(self,file):
        data = scipy.io.loadmat(file)
        X = data.get('ReduTIMotionCell')
        return X

    def showPlot(self, frame_id, fish_id):
        # d = self.data[0,fish_id-1][:, 0:3]
        # point_id = frame_id - self.frame_begin
        #
        # ax = self.fig.gca(projection='3d')
        # ax.scatter(d[:, 0], d[:, 1], d[:, 2], color=[1, 0.1, 0.1], marker='.', alpha=0.5, s=0.2)
        # ax.plot([d[point_id, 0]], [d[point_id, 1]], [d[point_id, 2]], 'b.', marker='.', markersize=6.5, alpha=0.9)
        #
        # ax.set_xlabel('X Label')
        # ax.set_ylabel('Y Label')
        # ax.set_zlabel('Z Label')
        # self.draw()


        d = self.data[0,fish_id-1][:, 0:2]
        point_id = frame_id - self.frame_begin

        ax = self.figure.add_subplot(111)
        ax.hold(False)

        ax.plot(d[:, 0], d[:, 1], 'r.', alpha=0.5, markersize=2)
        ax.hold(True)
        ax.plot(d[point_id, 0], d[point_id, 1], 'b.', alpha=0.9, markersize=5)

        ax.hold(False)

        self.draw()




