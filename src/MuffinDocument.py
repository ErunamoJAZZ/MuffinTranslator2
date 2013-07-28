'''
Created on 24/07/2013

@author: erunamo
'''
import os
import threading, time
import codecs
from PySide import QtCore, QtGui

class DocumentManagement(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
        
###############################################
########   AUTO-GUARDADO, MULTIHILO   #########
class AutoGuardado(threading.Thread):
    '''
    AutoGuardado: Clase que hereda de Therad, y 
    guarda cada cierto tiempo los datos.
    @param _Text: un objeto tipo DocumentManagement
    '''
    def __init__(self, _Text):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.__Text=_Text
        self.seguir_guardando=self.__Text.esta_guardado
        
    def run(self):
        '''
        Inicia Bucle de auto-guardado. 
        '''
        while True : #si ya se ha guardado
            time.sleep(30)
            if self.seguir_guardando:
                self.__Text.SaveFile(self.__Text.path)
                print ("» Guardado Automatico...(30seg) "+self.getName() )
            else:
                print (self.getName()+" is dead X.x")
                break
    
    def kill(self):
        '''
        Hace que el bucle se termine en la proxima iteración.
        '''
        self.seguir_guardando=False
        print (self.getName()+" pronto... morirá u.u")