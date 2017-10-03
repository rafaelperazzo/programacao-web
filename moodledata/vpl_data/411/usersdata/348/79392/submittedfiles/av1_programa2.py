# -*- coding: utf-8 -*-

x = float(input( 'informe metodo de pagamento: '))
x1 = float(input( 'valor da compra: '))
 
 # metodos de pagamento
 #1 15% desconto a vista x==1
 #2 10% desconto cartao x==2 
 #3 duas vezes sem juros x==3
 #4 duas vezes com 10% juros x==4
 
if x==1:
    x2 = x1*(15/100)
    x1 = x1 - x2
    print ('1')
    print('%.2f' %x1)
    
elif x==2:
    x3 = x1*(10/100)
    x1 = x1 - x3
    print ('2')
    print('%.2f' %x1)
    
   
elif x==3:
    x1 = x1
    print ('3')
    print('%.2f' %x1)
 
elif x==4:
    x4 = x1*(10/100)
    x1 = (x1+x4)
    print ( '4')
    print('%.2f' %x1)
   
    
    
    
    
    
    
    
    