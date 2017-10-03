# -*- coding: utf-8 -*-
n=int(input("Forneça um número: "))
#REPETIÇÃO
i=2
div=0
print()
print()
while i<n:
    if (n%i)==0:
        div=div+1
    i=i+1
if div>0:
    print("É PRIMO")
else:
    print("NÃO É PRIMO")
    