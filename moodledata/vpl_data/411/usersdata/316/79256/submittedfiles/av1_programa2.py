# -*- coding: utf-8 -*-
print('códigos de pagamento: 1 - À vista em dinheiro ou cheque. 2 - À vista no cartão crédito. 3 - Em duas vezes, preço normal de etiqueta. 4 - Em duas vezes, com jueros de 10%.')
vl=int(input('Digite o valor dos produtos:'))
fp=int(input("Digite o código de pagamento:"))
if fp=1:
    t=(vl-(vl*0.15))
elif fp=2:
    t=(vl-(vl*0.10))
elif fp=3:
    t=vl
else: 
    t=(vl+(vl*0.10)

