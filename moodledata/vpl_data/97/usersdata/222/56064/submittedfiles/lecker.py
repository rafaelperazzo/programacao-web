# -*- coding: utf-8 -*-

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                con=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[]
b=[]
n=int(input('n:'))
for i in range(0,n,1):
    a.append(int(input('a:')))
for i in range(0,n,1):
    b.append(int(input('b:')))
if lecker(a):
    print('S')
else:('N')
if lecker(b):
    print('S')
else:('N')