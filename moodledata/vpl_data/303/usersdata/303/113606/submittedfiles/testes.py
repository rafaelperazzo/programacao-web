nome=str(input('DIGITE O NOME DO USUÁRIO:'))
n=int(input('DIGITE A QUANTIDADE DE CARACTERES:'))

senha=[]

for i in range(0,n,1):
    senha.append(int(input('DIGITE UM NUMERO P SENHA:')))
    
cont=0
for i in range(0,n-1,1):
    if senha[i] == senha[i+1]:
        cont+=1
while cont ==1 or cont>1:
    print('SENHA INVÁLIDA')
    for i in range(0,n,1):
        senha.append(int(input('DIGITE UM NUMERO P SENHA:')))
    cont=0
    for i in range(0,n-1,1):
        if senha[i] == senha [i+1]:
            cont +=1
else:
    print('SENHA VALIDA')