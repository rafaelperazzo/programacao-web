def solicitaSimboloDoHumano():
    nome = input("digite seu apelido= ")
print ('\nolá %s escolha seu simbolo teclando 1 para X e 2 para O.'%nome)
simbolo = int(input(" "))
while simbolo>0:
    if simbolo==1:
        print("seu simbolo será= X")
        break
    else:
        print("seu simbolo será= O")
        break
