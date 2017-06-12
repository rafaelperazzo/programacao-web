# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade:'))

x=[]

for i in range(0,n,1):
    v=float(input('Digite o valor:'))
    x.append(v)
    
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+x[i]
    media=soma/len(a)
    return(media)    

print('%.2f'%media(x))
print('%.2f'%x[0])
print(x)
print('%.2f'%len(x)-1)
