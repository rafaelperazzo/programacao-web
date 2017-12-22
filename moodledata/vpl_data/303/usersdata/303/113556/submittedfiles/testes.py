# -*- coding: utf-8 -*#notas=[]
#for i in range(0,50,1):
 #   notas.append(float(input('DIGITE A NOTA%d[%d]:' %(i+1 , i)))



#somatorio=0

#for i in range(0,500,1):
#    if i%2!=0 and i%3==0:
#        somatorio+=i
    
#print(somatorio)


    
nome=str(input('Digite o nome do usuário:'))
n=int(input('Digite a quantidade de caracteres da senha:'))

senha=[]

for i in range(0,n,1):
    senha.append(int(input('Digite um numero para sua senha:')))
    
cont=0
for i in range(0,n-1,1):
    if senha[i]==senha[i+1]:
        cont+=1
if cont ==1:
    print('SENHA INVÁLIDA')
    for i in range(0,n,1):
    senha.append(int(input('Digite um numero para sua senha:')))
else:
    print('SENHA VÁLIDA')