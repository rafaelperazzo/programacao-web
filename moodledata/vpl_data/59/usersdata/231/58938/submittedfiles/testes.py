# -*- coding: utf-8 -*-






def vampiro(a):
    for i in range(0,len(a),1):
        if a[i]>(a[i]+1):
            return False
    return True
b=[]
n=2
for i in range(0,n,1):
    valor=int(input('vv:'))
    b.append(valor)
if vampiro(b):
    print('s')
else:
    print('n')




    
   
        
    
