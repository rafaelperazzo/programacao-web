# -*- coding: utf-8 -*-
p=int(input("Digite P: "))
q=int(input("Digite Q: "))
while p > q:
    p=int(input("Digite P: "))
    q=int(input("Digite Q: "))
for i in range (0,100,1):
    div1=p//(10**i)
    if  1 <= div1 <= 9:
        digp=i + 1
        break
    else:
        div1=0
for j in range (0,100,1):
    div2=q//(10**j)
    if 1 <= div2 <= 9:
        digq=j + 1
        break
    else:
        div2=0
pot=digq-digp
rep=digq-digp+1
cont=0
l=digq
for t in range (0,rep,1):
    n=(q//(10**pot)) - (q//(10**l)*10)
    if q == n:
        cont = cont + 1
        break
    else:
        pot=pot-1
        l=l-1
if cont == 0:
    print ("N")
if cont == 1:
    print ("S")
