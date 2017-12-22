# -*- coding: utf-8 -*-
avenida=[]
a=0
#restriçõe+qual é a dimensão da  minha matriz
m= int(input('Digite o numero de linhas: '))
n=int (input('Digite o numero de colunas: '))
while 1000>m<2 or 2>n>1000:
    m= int(input('Digite o numero de linhas: '))
    n=int (input('Digite o numero de colunas: '))
#matriz das quadras com o preço    
for i in range (0,m,1):
    a=[]
    for j in range (n-1,-1,-1):
        a.append(float(input('Digite o valor da quadra%d%d: ' % ((i+1),(j+1)))))
    avenida.append(a)
# função que calcula o menor valor de quadras

def valormim(b):
    for w in range(0,(len(b)-1),1):
        while sum(b[w])< sum(b[w+1]):
            a=sum(b[w])
        return a
        
print (valormim(avenida))
            
            
            
            
            
        