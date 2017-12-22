# -*- coding: utf-8 -*#notas=[]
#for i in range(0,50,1):
 #   notas.append(float(input('DIGITE A NOTA%d[%d]:' %(i+1 , i)))


nome=input('Digite o nome de usuário:')

verifica=[]
n=str(input('Digite a senha:'))
verifica.append(n)

for i in range(1,verifica,1):
    if verifica[i-1]==verifica[i]:
        print('SENHA INVÁLIDA')
    
    