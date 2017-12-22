# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
linhas = []
colunas = []
for linhas in range (0,3,1):
    for colunas in range (0,3,1):
        print('%d %d ' % (linhas,colunas))
print(linhas[0],colunas[0])