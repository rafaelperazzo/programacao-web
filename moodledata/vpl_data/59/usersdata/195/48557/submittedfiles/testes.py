# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
i=1
for i in range (1,n+1,1):
    x=i/(i*i)
    if i%2!=0:
        soma=soma+x
    else:
        soma=soma-x
print('s: %.5f' %soma)        
    
