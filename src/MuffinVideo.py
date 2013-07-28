# -*- coding: utf-8 -*-

#based: https://gist.github.com/PyYoshi/5260187

'''
Created on 24/07/2013

@author: erunamo
'''


import sys
from subprocess import PIPE

from mplayer.core import Player
from mplayer import misc
from os import name

if name == 'nt':
    import ctypes

from PySide import QtCore, QtGui
# thanks: http://qt-project.org/wiki/Signals_and_Slots_in_PySide_Japanese
QtCore.pyqtSignal = QtCore.Signal
QtCore.pyqtSlot = QtCore.Slot

__all__ = ['QPlayerView']

class QtPlayer(Player):
    def __init__(self, args=(), stdout=PIPE, stderr=None, autospawn=True):
        super(QtPlayer, self).__init__(args, autospawn=False)
        self._stdout = _StdoutWrapper(handle=stdout)
        self._stderr = _StderrWrapper(handle=stderr)
        if autospawn: self.spawn()


class QPlayerView(QtGui.QWidget):
    eof = QtCore.Signal(int)

    def __init__(self, parent=None, volume=None, slider=None):
        super(QPlayerView, self).__init__(parent)
        self._player = self._create_mplayer()
        self.slider = slider
        self.volume = volume
        self.fileVideo = ''
        self._player.stdout.connect(self._handle_data)
        self.destroyed.connect(self._on_destroy)
        #default values
        
    def _create_mplayer(self, args=(), stderr=None):
        return QtPlayer(('-msglevel', 'global=6', '-fixed-vo', '-fs', '-volume', 10,
                          '-vo','gl', '-nofontconfig', '-wid', int(self._get_winId())) + args, stderr=stderr)
    def _on_destroy(self):
        self._player.quit()

    def _handle_data(self, data):
        if data.startswith('EOF code:'):
            code = data.partition(':')[2].strip()
            self.eof.emit(int(code))

    def resizeEvent(self, event):
        pass

    def load_video(self):
        self.fileVideo, _ = (QtGui.QFileDialog.getOpenFileName(self, 'Open file',''))
        #print(self.fileVideo)
        self.pause_clicked()

    def play_video (self):
        self._player.loadfile(self.fileVideo)#"/home/erunamo/videos/q.mkv"
        self._player.volume = 50
        self.volume.setValue(50)
    
    
    def pause_clicked(self):
        if self._player.is_alive():
            if self.fileVideo == '':
                self.load_video()
            else:
                self._player.pause()
                self.setSlider()
        else:
            self._player = self._create_mplayer()
            self.play_video()
            self.set_vol_clicked()
            self.slider.setValue(0)
    
    def stop_clicked(self):
        self._player.quit()
        self.slider.setValue(0)

    def set_vol_clicked(self):
        vol = self._player.volume
        if vol != None:
            self._player.volume = self.volume.value()
    
    def set_pos(self):
        if self._player.is_alive():
            self._player.percent_pos = self.slider.value()
    
    def onAdvanceVideo(self, time=5):
        self._player.seek(time)
        self.setSlider()
        
    
    def onBackVideo(self, time=-5):
        self._player.seek(time)
        self.setSlider()
        
    
    def setSlider(self):
        p100 = self._player.percent_pos
        if p100 != None:
            self.slider.setSliderPosition(int(p100))

    
    def _get_winId(self):
        '''Hack from: https://bugreports.qt-project.org/browse/PYSIDE-46 '''
        if name == 'nt':
            ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
            ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object]
            return ctypes.pythonapi.PyCapsule_GetPointer(self.winId(), None)
        else:
            return self.winId()


class _StderrWrapper(misc._StderrWrapper):

    def __init__(self, **kwargs):
        super(_StderrWrapper, self).__init__(**kwargs)
        self._notifier = None

    def _attach(self, source):
        super(_StderrWrapper, self)._attach(source)
        self._notifier = QtCore.QSocketNotifier(self._source.fileno(),
                                                QtCore.QSocketNotifier.Read)
        self._notifier.activated.connect(self._process_output)

    def _detach(self):
        self._notifier.setEnabled(False)
        super(_StderrWrapper, self)._detach()

class _StdoutWrapper(_StderrWrapper, misc._StdoutWrapper):
    pass

