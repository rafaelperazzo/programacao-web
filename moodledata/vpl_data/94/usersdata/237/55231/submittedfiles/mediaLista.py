# -*- coding: utf-8 -*-
n=int(input("Digite o numero de elementos: "))
a=[]
for i in range (0,n,1):
    a.append(float(input("Digite o digito: ")))
print('%.2f'%a[0])
print('%.2f'%a[len(a)-1])
r=0
for i in range(0,len(a),1):
    r=r+a[i]
print('%.2f'%(r/n))
print(a)


