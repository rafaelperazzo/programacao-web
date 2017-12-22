# -*- coding: utf-8 -*#notas=[]
#for i in range(0,50,1):
 #   notas.append(float(input('DIGITE A NOTA%d[%d]:' %(i+1 , i)))



#somatorio=0

#for i in range(0,500,1):
#    if i%2!=0 and i%3==0:
#        somatorio+=i
    
#print(somatorio)

lista1=[]

n=int(input('Digite a quantidade de termos da lista:'))

for i in range(0,n,1):
    lista1.append(int(input('Digite um elemento:')))
    
for i in(0,len(lista1),1):
    dp=sum(((lista1[i]-(sum(lista1)//2)))**2)
    
print(m)