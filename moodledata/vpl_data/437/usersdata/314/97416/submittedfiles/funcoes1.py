# -*- coding: utf-8 -*-
  #escreva o código da função crescente aqui

def crescente (a,b,c):
    maiora=a[0]
    maiorb=b[0]
    maiorc=c[0]    
    for i in range(0,n,1):
        if a[i]>maiora or b[i]>maiorb or c[i]>maiorc:
            print('S')
#escreva as demais funções

#escreva o programa principal
n=int(input('Digite n: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(int(input('Digite os valore de a: ')))
    b.append(int(input('Digite os valore de b: ')))
    c.append(int(input('Digite os valore de c: ')))
print(crescente(a,b,c))  
