# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:10:04 2017

@author: Ruan Carlos 
"""
#importando biblioteca:

import math

print("Bem vindo ao python")

#Atribuindo valores as variaveis:

erro = (1*10**(-5))
a = 1
c = 1
r=1
sigma=40000
e=30*10**(6)

#recebendo dados do usuario:

ecent = float(input("digite a ecentricidade: "))
l= float(input("digite o comprimento da viga analisada: "))

#função pcr:

pcr=((((math.pi)**2)*e*a)/(l/r)**2)
p0= pcr/2
k=0

while(True):

    #função principal:
    #dividindo a função em blocos:
    
    z = ((p0/e)**(0.5))   
    x = (1+(ecent)*(1/math.cos((l/2)*z)))
    
    #calculando a função
    
    fp = p0 - (sigma/x)
    
    #dividindo a derivada da função em blocos:
    
    n = (l*sigma*ecent)*(1/math.cos((l/2)*(p0/e)**0.5))
    m = math.tan((l/2)*(p0/e)**0.5)
    o = (4*(e*p0)**0.5)
    p = (1+ecent*(1/math.cos((l/2)*(p0/e)**0.5)))**2

    #Calculando o valor da função derivada:
        
    fp2 = 1+(n*m)/(p*o)
    
    #Contando as interações:
    
    print('Iteração ' + str(k))
    k=k+1
    
    x2 = p0 - (fp/fp2)
    print (p0,x2)
    
    #Definindo criterio de parada:
    
    if abs(p0-x2)<erro:
        break
    
    #Restrição do intem 4, se a raiz maior qu Pcr,faça:
    if (x2>pcr):
        x2=(p0+pcr)/2
    
    p0=x2
    
#substituindo na função pra comprovar a raiz:
    
z = ((x2/e)**(0.5))   
x = (1+(ecent)*(1/math.cos((l/2)*z)))
    
fp = p0 - (sigma/x)
print("O numero substituido na raiz é :",fp)
print("A raiz é = ", x2)
print("A função chegou a esses valores após '%' interações",%fk)

