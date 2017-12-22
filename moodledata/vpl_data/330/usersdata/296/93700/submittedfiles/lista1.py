# -*- coding: utf-8 -*-
n = int(input("Digite o valor de n: "))
a = []
for i in range (0,n,1):
    a.append(int(input("Digite um valor: ")))
spares = 0
simpares = 0
qpares = 0
qimpares = 0
for i in range (0,n,1):
   if a[i] % 2  == 0:
       qpares = qpares + 1
       spares = spares + a[i]
   else:
       simpares = simpares + 1
       qimpares = qimpares + a[i]
print(qimpares)
print(spares)
print(simpares)
print(qpares)
print(a)


 
       
       
    

    


