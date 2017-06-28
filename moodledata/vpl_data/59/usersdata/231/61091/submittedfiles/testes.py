# -*- coding: utf-8 -*
n=4
a=[]
for i in range(0,n,1):
    valor=int(input('digite número:'))
    a.append(valor)
m=int(str(a[0])+str(a[1])+str(a[2])+str(a[3]))
k=int(str(a[1])+str(a[0]))
l=int(str(a[2])+str(a[3]))
u=int(str(a[2])+str(a[1]))
w=int(str(a[0])+str(a[3]))
g=int(str(a[2])+str(a[0]))
p=int(str(a[1])+str(a[3]))
if m==(k*l):
    print('número vampiro')
elif m==(u*w):
    print('número vampiro')
elif m==(g*p):
     print('número vampiro')
else:
    print('não é vampiro')



    
   
        
    
