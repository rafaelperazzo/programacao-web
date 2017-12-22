# -*- coding: utf-8 -*-
n = int(input("Digite o valor de n: "))
a = []
for i in range (0,n,1):
    a.append(input("Digite um valor: "))
Spares = 0
Simpares = 0
Qpares = 0
Qimpares = 0
for i in range (0,n,1):
   if [ai] % 2  == 0:
       Spares = Spares + 1
       Qpares = Qpares + a[i]
   else:
       Simpares = Simpares + 1
       Simpares = Simpares + a[i]
print(Spares)
print(Qpares)
print(Simpares)
print(Qimpares)
print(a)
 
       
       
    

    


