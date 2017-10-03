# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
saque =int=(input('digite o valor do saque'))
if saque >= 20:
   print((saque-saque//20)/20)
   saque=(saque//20) 
else:

 print(0)
if saque >= 10:
   print((saque-saque//10)/10)
   saque=(saque//10)  
else:

 print(0)
if saque >= 5:
   print((saque-saque//5)/5)
   saque=(saque//5)
else:

 print(0)
if saque >= 2:
   print((saque-saque//2)/2)
   saque=(saque//2) 
else:

 print(0)
print(saque)










