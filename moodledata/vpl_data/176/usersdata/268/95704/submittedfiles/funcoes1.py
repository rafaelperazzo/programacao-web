# -*- coding: utf-8 -*-

def crescente (a):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(a),1):
        if (a[i]>a[i-1]):
             cont=cont+1
        else:
             break
    if cont==len(a)-1:
        return(True)
    else:
        return(False)

#escreva as demais funções
def decrescente (a):
    cont=0
    for i in range(1,len(a),1):
        if (a[i]<a[i-1]):
             cont=cont+1
        else:
             break
    if cont==len(a)-1:
        return(True)
    else:
        return(False)
def consecutivo (a):
    cont=0
    for i in range(1,len(a),1):
        if (a[i]==a[i-1]):
             break
        else:
             cont=cont+1
    if cont==len(a)-1:
        return(False)
    else:
        return(True)





#escreva o programa principal

n=int(input('Digite o numero de termos das listas: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    valor_a=int(input('Digite o termo de a : '))
    a.append(valor_a)
for i in range(0,n,1):
    valor_b=int(input('Digite o termo de b : '))
    b.append(valor_b)
for i in range(0,n,1):
    valor_c=int(input('Digite o termo de c : '))
    c.append(valor_c)
if crescente(a)==True:
    print('S')
if crescente(a)==False:
    print('N')
if decrescente(a)==True:
    print('S')
if decrescente(a)==False:
    print('N')
if consecutivo(a)==True:
    print('S')
if consecutivo(a)==False:
    print('N')
if crescente(b)==True:
    print('S')
if crescente(b)==False:
    print('N')
if decrescente(b)==True:
    print('S')
if decrescente(b)==False:
    print('N')
if consecutivo(b)==True:
    print('S')
if consecutivo(b)==False:
    print('N')
if crescente(c)==True:
    print('S')
if crescente(c)==False:
    print('N')
if decrescente(c)==True:
    print('S')
if decrescente(c)==False:
    print('N')
if consecutivo(c)==True:
    print('S')
if consecutivo(c)==False:
    print('N')
print(a)
print(b)
print(c)