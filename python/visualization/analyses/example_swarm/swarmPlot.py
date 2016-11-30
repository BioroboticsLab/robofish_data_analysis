import scipy.io
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class SwarmPlot(FigureCanvas):
    def __init__(self, file, frame_begin):
        self.fish_id = 1
        self.data = self.__load_data(file)
        self.frame_begin = frame_begin

        self.fig = plt.figure()

        FigureCanvas.__init__(self, self.fig)


    def __load_data(self,file):
        data = scipy.io.loadmat(file)
        X = data.get('ReduState')
        return X

    def showPlot(self, frame_id, fish_id):

        d = self.data[:,0:2]
        point_id = frame_id - self.frame_begin

        ax = self.figure.add_subplot(111)
        ax.hold(False)

        ax.plot(d[:, 0], d[:, 1], 'r.', alpha=0.5, markersize=2)
        ax.hold(True)
        ax.plot(d[point_id, 0], d[point_id, 1], 'b.', alpha=0.9, markersize=5)

        ax.hold(False)

        self.draw()



