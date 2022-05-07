import numpy as np
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg

import struct
import pyaudio
#from scipy.fftpack import fft

import sys
import time


class AudioStream(object):
    def __init__(self):

        # pyqtgraph stuff
        pg.setConfigOptions(antialias=True)
        self.traces = dict()
        #self.app = QtWidgets.QApplication(sys.argv)
        self.win = pg.GraphicsLayoutWidget()#title='Spectrum Analyzer')
        self.win.show()
        #self.win.setWindowTitle('Spectrum Analyzer')
        #self.win.setGeometry(5, 115, 1910, 1070)

        self.waveform = self.win.addPlot(
            row=1, col=1 #, axisItems={'bottom': wf_xaxis, 'left': wf_yaxis},
        )
        
        self.waveform.hideAxis('bottom')
        self.waveform.hideAxis('left')

        # pyaudio stuff
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )
        # waveform and spectrum x points
        self.x = np.arange(0, 2 * self.CHUNK, 2)

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            #QtGui.QApplication.instance().exec_()
            QtWidgets.QApplication.instance().exec_()

    def set_plotdata(self, name, data_x, data_y):
        if name in self.traces:
            self.traces[name].setData(data_x, data_y)
        else:
            self.traces[name] = self.waveform.plot(pen='c', width=3)
            self.waveform.setYRange(0, 255, padding=0)
            self.waveform.setXRange(0, 2 * self.CHUNK, padding=0.005)


    def update(self):
        wf_data = self.stream.read(self.CHUNK)
        wf_data = struct.unpack(str(2 * self.CHUNK) + 'B', wf_data)
        wf_data = np.array(wf_data, dtype='b')[::2] + 128
        self.set_plotdata(name='waveform', data_x=self.x, data_y=wf_data,)
        #self.set_plotdata(data_x=self.x, data_y=wf_data)

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(20)
        self.start()


#DEBUG
if __name__ == '__main__':
    audio_app = AudioStream()
    audio_app.animation()