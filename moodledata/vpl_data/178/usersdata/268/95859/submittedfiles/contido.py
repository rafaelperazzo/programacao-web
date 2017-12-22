# -*- coding: utf-8 -*-

def resposta(a,b):
     cont=0
     for i in range(0,len(a),1):
         if a[i] in b:
             for m in range(0,len(b),1):
                 if a[i]==b[m]
                 cont=cont+1
         
     return(cont)
        
    
m=int(input('Digite o tamanho da list de a : '))
n=int(input('Digite o tamanho da list de b : '))

a=[]
b=[]

for i in range(0,m,1):
    valora=int(input('Digite o termo de a : '))
    a.append(valora)
for i in range(0,n,1):
    valorb=int(input('Digite o termo de b : '))
    b.append(valorb)

print(resposta(a,b))



