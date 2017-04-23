# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite um valor para f:'))
L=float(input('Digite um valor para L:'))
Q=float(input('Digite um valor para Q:'))
DeltaH=float(input('Digite um valor para o DeltaH:'))
v=float(input('Digite um valor para v:')) 
g=9.81
E=0.000002
pi=math.pi
D=((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**(1/5)
Rey=4*Q/(pi*D*v)
k=0.25/(math.log10(E/3.7*D+5.74/Rey**0.9))
print('O valor de D é:%.4f'%D)
print('O valor de Rey é: %.4f'%Rey)
print('O valor de k é:%.4f'%k)
