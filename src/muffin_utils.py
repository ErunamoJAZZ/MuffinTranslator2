# -*- coding: utf-8 -*-

#Código con cosas útiles para todo el programa

import os
import sys

__all__ = ['dir_']

#variables privadas
__dir = os.path.abspath(os.path.dirname(sys.argv[0]))


def dir_():
    '''Retorna el directorio del programa.
    Se usa para tener la ruta de las imagenes y eso.'''
    return __dir


