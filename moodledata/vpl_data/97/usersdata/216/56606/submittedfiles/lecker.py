# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de números na lista:'))
a=[]
b=[]

for i in range(0,n,1):
    c=int(input('Digite um valor para lista a:'))
    a.append(c)
    
for i in range(0,n,1):
    d=int(input('Digite um valor para lista b:'))
    b.append(d)

def lecker(x):
    cont=0
    for i in range(0,len(x),1):
        if (i==0):    
            if ((x[i])>(x[i+1])):
                cont=cont+1
        elif ((i==(len(x)-1))):
            if ((x[i])>(x[i-1])):
                cont=cont+1
        else:
            if ((x[i])>(x[i+1])) and ((x[i])>(x[i-1])):
                cont=cont+1
    if (cont==1):
        return True
    else:
        return False
            
if lecker(a):
    print('S')
else:
    print('N')

if lecker(b):
    print('S')
else:
    print('N')

print(a)
print(b)