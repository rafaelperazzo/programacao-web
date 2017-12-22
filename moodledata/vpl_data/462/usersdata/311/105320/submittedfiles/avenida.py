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
        a.append(int(input('Digite o valor da quadra%d%d: ' % ((i+1),(j+1)))))
    avenida.append(a)
# função que calcula o menor valor de quadras
def menor(b):
    for w in range (0,len(b)-1,1):
        if len(b)==2:
            if sum(b[0])  < sum(b[1]):
                return (sum(b[0]))
            else:
                return (sum(b[1]))
        if len (b)==3:
            if sum(b[w])<sum(b[w+1]):
                return (sum(b[w]))
            if sum(b[w+1])<sum(b[w]):
                return (sum(b[w+1])
            if sum(b[w+1])< sum(b[w+2]):
                return (sum(b[w+1]))
            else:
                return (sum(b[w+2]))
        
        
        
print (menor(avenida))
            
            
            
            
            
        