# -*- coding: utf-8 -*-






def vampiro(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]>(a[i]+1):
            cont=cont+1
    return cont    
b=[]
n=3
for i in range(0,n,1):
    valor=int(input('vv:'))
    b.append(valor)
if vampiro(b)==2:
    print('s')
else:
    print('n')




    
   
        
    
