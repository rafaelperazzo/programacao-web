# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:10:04 2017

@author: Carlos Manoel
"""

import math
#import matplotlib.pyplot as plt
#from pylab import *

print("Bem vindo ao python")

#dando valores as variaveis

erro = (1*10**(-5))
a = 1
c = 1
r=1
sigma=40000
e=30*10**(6)

ecent = float(input("digite a ecentricidade: "))
l= float(input("digite o comprimento: "))

#função pcr:

pcr=((((math.pi)**2)*e*a)/(l/r)**2)
p0= pcr/2
#x2=0
p01=p0
k=0

while(True):

    #função principal:
    #dividindo a função em blocos:
    
    z = ((p0/e)**(0.5))   
    x = (1+(ecent)*(1/math.cos((l/2)*z)))
    
    #calculando a função
    fp = p0 - (sigma/x)
    #print(fp)
    #print("p0",p0)
    #dividindo a derivada da função em blocos:
    n = (l*sigma*ecent)*(1/math.cos((l/2)*(p0/e)**0.5))
    m = math.tan((l/2)*(p0/e)**0.5)
    o = (4*(e*p0)**0.5)
    p = (1+ecent*(1/math.cos((l/2)*(p0/e)**0.5)))**2

    #calculando na derivada:
        
    fp2 = 1+(n*m)/(p*o)
    
    #contando as interações
    print('Iteração ' + str(k))
    k=k+1
    
    x2 = p0 - (fp/fp2)
    print (p0,x2)
    #print (abs(p0-x2))
    if abs(p0-x2)<erro:
        break
    print(x2)
    p0=x2
    
#substituindo na função pra comprovar a raiz:
    
z = ((x2/e)**(0.5))   
x = (1+(ecent)*(1/math.cos((l/2)*z)))
    
fp = p0 - (sigma/x)
print("O numero substituido na raiz é :",fp)
print("A raiz é = ", x2)
print("o numero de interações é", k)

#a=linspace(x2-1000,x2+1000,100)
#fp = p0 - (sigma/(1+(ecent)*(1/math.cos((l/2)*((a/e)**(0.5))))))
#plt.plot(a,fp)