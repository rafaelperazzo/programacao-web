# -*- coding: utf-8 -*-
N=int(input("Digite o número de postos de ágoa: "))
M=int(input("Digite a distancia intermediaria maxima: "))
o=[]
c=0
for i in range (0,N,1):
    o.append(int(input("Digite a distancia: ")))
for i in range (1,len(o),1):
    if o[i]-o[i-1]>=M:
        c=c+1
if c==0:
    print("S")
else:
    print("N")
        

