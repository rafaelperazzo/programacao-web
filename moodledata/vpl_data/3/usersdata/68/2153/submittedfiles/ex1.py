from __future__ import division

#ENTRADA:
a = ('Digite a:')
b = ('Digite b:')
c = ('Digite c:')

#PROCESSAMENTO E SAIDA:
Delta = (b**2) - (4*a*c)
if Delta<0:
    print ('SRR')

else :
    x1=((-b) + (Delta**0.5))/(2*a)
    x2= ((-b) - (Delta**0.5))/(2*a)
    print ('x1 é igual:%.1f'%x1)
    print ('x2 é igual:%.1f'%x2)
    
