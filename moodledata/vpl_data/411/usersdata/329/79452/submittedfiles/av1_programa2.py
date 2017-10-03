# -*- coding: utf-8 -*-
produto = float(input("digite o valor do produto= "))
dinheirooucheque = (-produto*0.15)+produto
cartaodecredito = (-produto*0.10)+produto
duasvezessemjuros = produto
duasvezescomjuros = (produto*0.10)+produto
1 = dinheirooucheque
2 = cartaodecredito
3 = duasvezessemjuros
4 = duasvezescomjuros
formadepagamento = int(input("digite a forma de pagamento= "))
if 1:
    print('%.2f'% dinheirooucheque)
elif 2:
    print('%.2f' % cartaodecredito)
elif 3:
    print('%.2f' % duasvezessemjuros)
else :
    print('%.2f' % duasvezescomjuros)
    
            
            
        
            
