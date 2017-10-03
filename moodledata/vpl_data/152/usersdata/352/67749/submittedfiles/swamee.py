# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
f=float(input('Digite o valor do fator de atrito f:'))
L=float(input('Digite o valor do comprimento L:'))
Q=float(input('Digite o valor da vazao Q:'))
H=float(input('Digite o valor da perda de carga H:'))
v=float(input('Digite o valor da velocidade cinematica v:'))

D=(((8*f*L*(Q*Q))/((math.pi**2)*9.81*H))**(0.2))
Rey=(4*Q)/(math.pi*D*v)
j=(0.000002/(3.7*D))+(5.74/(Rey**0.9))
k=0.25/((math.log10(j))**2)

print('O valor do diametro D é: %.4f'%D)
print('O numero de Reynolds é: %.4f'%Rey)
print('O fator de atrito inicial k é: %.4f'%k)