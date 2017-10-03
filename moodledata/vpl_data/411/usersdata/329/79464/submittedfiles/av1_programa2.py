# -*- coding: utf-8 -*-
produto = float(input("digite o valor do produto= "))
dinheirooucheque = (-produto*0.15)+produto
cartaodecredito = (-produto*0.10)+produto
duasvezessemjuros = produto
duasvezescomjuros = (produto*0.10)+produto
um = dinheirooucheque
dois = cartaodecredito
tres = duasvezessemjuros
quatro = duasvezescomjuros
formadepagamento = int(input("digite a forma de pagamento= "))
if um :
    print('%.2f'% dinheirooucheque)
elif dois :
    print('%.2f' % cartaodecredito)
elif tres :
    print('%.2f' % duasvezessemjuros)
else :
    print('%.2f' % duasvezescomjuros)
    
            
            
        
            
