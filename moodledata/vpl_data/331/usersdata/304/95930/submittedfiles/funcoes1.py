# -*- coding: utf-8 -*-

def crescente(a):
    #escreva o código da função crescente aqui
    cont = 0
    for i in range(1, len(a) ,1):
        if (a[i]>a[i-1]):
            cont=cont+1
        else:
            break
        if cont==len(a)-1:
            return(S)
        else:
            return(N)

#escreva as demais funções
def decrescente (a):
    cont=0
    for i in range(1,len(a),1):
        if (a[i]<a[i-1]):
            cont=cont+1
        else:
            break
        if cont==(len(a)-1):
            return(S)
        else:
            return(N)
def consecutivo(a):
    cont=0
    for i in range(1,len(a),1):
        if (a[i]==a[i-1]):
            break
        else:
            cont=cont+1
        if cont==(len(a)-1):
            return(N)
        else:
            return(S)





#escreva o programa principal

n=int(input('n: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    v_a=int(input('a: '))
    a.append(v_a)
for i in range(0,n,1):
    v_b=int(input('b: '))
    b.append(v_b)
for i in range(0,n,1):
    v_c=int(input('c: '))
    c.append(v_c)
    
if crescente(a)==S:
    print('S')
else:
    print('N')
if decrescente(a)==S:
    print('S')
else:
    print('N')
if consecutivo(a)==S:
    print('S')
else:
    print('N')
if crescente(b)==S:
    print('S')
else:
    print('N')
if decrescente(b)==S:
    print('S')
else:
    print('N')
if consecutivo(b)==S:
    print('S')
else:
    print('N')
if crescente(c)==S:
    print('S')
else:
    print('N')
if decrescente(c)==S:
    print('S')
else:
    print('N')
if consecutivo(c)==S:
    print('S')
else:
    print('N')
    