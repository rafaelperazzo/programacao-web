# -*- coding: utf-8 -*-

# a vista dinheiro ou cheque, 15% de desconto
# a vista cartao, 10% de desconto
# em duas vezes, valor sem juros
# em duas vezes, valor mais 10%

d= float(input('Digite o valor da compra: '))
p= int(input('Digite a quantidade de parcelas: '))

v1= d - (d*0.15)
v2= d - (d*0.10)
v3= d + (d*0.10)

if p==1:
    print('Opção a vista em dinhero ou cheque digite: 1') 
    print('Opção a vista no cartão digite: 2')
    o= int(input('digite a opçao de pagamento: ' ))
    if o==2:
        print(v2)
    elif o==1:
        print(v1)
    elif o>2:
        print('Opção Invalida')
    else:
        print('Opção Invalida')













    
    