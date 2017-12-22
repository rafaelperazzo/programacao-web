# -*- coding: utf-8 -*-

#Função que calcula a altura do degrau
def altura(deg):
    for i in range (0,n,1):
        altura=abs(int(deg[i]-deg[i+1]))
        return altura








#main.py
a=[]
n=int(input('Digite um numero abaixo: '))
while (n<2):
    n=int(input('Digite um numero abaixo: '))
for i in range (0,n,1):
    a.append(input('Digite o numero%d: ' %(i+1)))
print (altura(a))
    


    

