# -*- coding: utf-8 -*-
n=int(input('digite n: '))
a=[]
for i in range(0,n,1):
    x=int(input('digite: '))
    a.append(x)
contpar=0
contimpar=0
somapar=0
somaimpar=0
for r in range(0,len(a),1):
    if (a[r]/2)==0:
        somapar=somapar+a[r]
        contpar=contpar+1
    if (a[r]/2)==1:
        somaimpar=somaimpar+a[r]
        contimpar=contimpar+1
    print(a[r])    
print(somaimpar)
print(somapar)
print(contimpar)
print(contpar)
print(a)
