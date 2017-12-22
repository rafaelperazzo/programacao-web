# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
linhas = []
colunas = []
for linhas in range (0,3,1):
    for colunas in range (0,3,1):
        print('|%d %d|,|%d %d|,|%d %d|,\n |%d %d|,|%d %d|,|%d %d|\n|%d %d|,|%d %d|,|%d %d|' % (linhas,colunas))