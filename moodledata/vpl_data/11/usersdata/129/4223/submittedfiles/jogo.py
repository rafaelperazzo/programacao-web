# -*- coding: utf-8 -*-
from __future__ import division
import math
CV=input('Digite o valor de CV: ')
CE=input('Digite o valor de CE: ')
CS=input('Digite o valor de CS: ')
FV=input('Digite o valor de FV: ')
FE=input('Digite o valor de FE: ')
FS=input('Digite o valor de FS: ')
if (CV*3)+(CE)>(FV*3)+(FE):
    print ('C')
elif (CV*3)+(CE)<(FV*3)+(FE):
    print ('F')
else:
    if CS>FS:
        print ('C')
    elif CS<FS:
        print ('F')
    else :
        print ('=')
