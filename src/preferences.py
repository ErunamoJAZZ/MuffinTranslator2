# -*- coding: utf-8 -*-

'''
Created on 24/07/2013

@author: erunamo
'''

import configparser
from os import name



def singleton(cls):
    '''' from: http://www.python.org/dev/peps/pep-0318/#examples '''
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class preferences():
    
    def __init__(self):
        '''
        Default preferences
        '''
        self.__config = configparser.ConfigParser()
    
        ###############
        self.mplayer_vo = 'gl'
        self.time_seek = 3
        self.tome_auto_save = 30
        self.font_size = 12
        
        self.ctrl_1 = ''
        self.ctrl_2 = ''
        self.ctrl_3 = ''
        self.ctrl_4 = ''
        self.ctrl_5 = ''
        self.ctrl_6 = ''
        self.ctrl_7 = ''
        self.ctrl_8 = ''
        self.ctrl_9 = ''
        self.ctrl_0 = ''
        
        
        
        if name == 'nt':
            self.mplayer_path = 'mplayer.exe'
            self.mplayer_ao = 'dsound'
            self.font = 'Times New Roman'
            self.last_path = ''
            self.default_path = ''
        else:
            self.mplayer_path = 'mplayer'
            self.mplayer_ao = 'pulse'
            self.font = 'DejaVu Serif'
            self.last_path = ''
            self.default_path = ''
        
        ###############
    
    
    def load_preferences(self):
        pass
    
    def save_preferences(self):
        with open('example.ini', 'w') as configfile:
            self.__config.write(configfile)


