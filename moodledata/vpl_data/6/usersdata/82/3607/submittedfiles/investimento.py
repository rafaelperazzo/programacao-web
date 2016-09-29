# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
I = input ('Digite o valor do invertimento:')
T = input ('Taxa crescimento percentual:')

#PROCESSAMENTO
Ia = I+(T*I)
Ib = Ia+(T*Ia)
Ic = Ib+(T*Ib)
Id = Ic+(T*Ic)
Ie = Id+(T*Id)
If = Ie+(T*Ie)
Ig = If+(T*If)
Ih = Ig+(T*Ig)
Ii = Ih+(T*Ih)
Ij = Ii+(T*Ii)

#SAIDA
print ('%.2f' %Ia)
print ('%.2f' %Ib)
print ('%.2f' %Ic)
print ('%.2f' %Id)
print ('%.2f' %Ie)
print ('%.2f' %If)
print ('%.2f' %Ig)
print ('%.2f' %Ih)
print ('%.2f' %Ii)
print ('%.2f' %Ij)




