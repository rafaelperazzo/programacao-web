# -*- coding: utf-8 -*-
  #escreva o código da função crescente aqui

def crescente (a,b,c):
    maiora=a[0]
    maiorb=b[0]
    maiorc=c[0]    
    for i in range(0,n,1):
        if a[i]>maiora or b[i]>maiorb or c[i]>maiorc:
            print('S')
        else:
            print('N')
#escreva as demais funções
def decrescente (a,b,c):
    menora=a[0]
    menorb=b[0]
    menorc=c[0]
    for i in range(0,n,1):
        if a[i]<menora or b[i]<menorb or c[i]<menorc:
            print('S decrescente')
        else:
            print('N')
def iguais (a,b,c):
    iguaisa=a[0]
    iguaisb=b[0]
    iguaisc=c[0]
    for i in range(0,n,1):
        if a[i]==iguaisa or b[i]==iguaisb or c[i]==iguaisc:
            print('S iguais')
        else:
            print('N')    

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
print(decrescente(a,b,c))
print(iguais(a,b,c))