# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
numa =int(input('1:'))
numb =int(input('2:'))
numc =int(input('3:'))
numd =int(input('4:'))  
nume =int(input('5:'))
numf =int(input('6:'))   
 
if numa<numb and numb<numc and numc<numd and numd<nume and nume<numf:
    print('C')
elif numa>numb and numb>numc and numc>numd and numd>nume and nume>numf:
    print('D')    
else:
    print('N')