# -*- coding: utf-8 -*-

# a vista dinheiro ou cheque, 15% de desconto
# a vista cartao, 10% de desconto
# em duas vezes, valor sem juros
# em duas vezes, valor mais 10%

print('OPÇÕES DE PAGAMENTO:')
print('A vista em dinhero ou cheque, com 15% de desconto digite: 1') 
print('A vista no cartão, com 10% de desconto digite: 2')
print('Em duas vezes, valor da etiqueta sem juros, digite: 3')
print('Em duas vezes, valor da etiqueta mais 10% de digite: 4')

d= float(input('Digite o valor da compra: '))
o= int(input('Digite a opção de pagamento: ' ))

if o==1:
    v1= d - (d*0.15)
    print('%.2f' %v1)
elif o==2:
    v2= d - (d*0.10)
    print('%.2f' %v2)
elif o==3:
    print('%.2f' %d)
elif o==4:
    v3= d + (d*0.10)
    print('%.2f' %v3)
else:
    print('Opção Invalida')














    
    