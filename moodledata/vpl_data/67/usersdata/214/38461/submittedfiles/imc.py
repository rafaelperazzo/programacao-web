# -*- coding: utf-8 -*-
def imc_calculo(P, A):
     if P/(A*A)<20:
         print '\nSeu IMC=%f você está abaixo do peso % (P/(A*A))'
    
    elif P/(A*A)>=20 and P/(A*A)/<=25:
         print '\nSeu IMC=%f você está no peso ideal' % (P/(A*A))
    
    elif P/(A*A)>=25 and P/(A*A)/<=30:
         print '\nSeu IMC=%f você está um pouco acima do peso' % (P/(A*A))

    elif P/(A*A)>=30 and P/(A*A)/<=40:
         print '\nSeu IMC=%f você está um pouco acima do peso' % (P/(A*A))

    elif P/(A*A)>40
         print '\nSeu IMC=%f você está um pouco acima do peso' % (P/(A*A))

def porcentagem(P, A):
     "\nvalor da porcetagen = %f" %((x/100)*y)

def menu():
    print '0=sair \n1=CALCULAR IMC \n2= CALCULA PORCENTAGEN:'

while true:
    opçao = menu()
    
    if opçao== 0:
     print "bye!" 
     break:  
     
    elif opçao== 1: 
        peso= float(input(' digite seu peso:'))
        altura= float(input(' digite sua altura:'))
        imc_calculo(peso, altura)
    
     elif opçao== 2:
         total= float(input('entre com o valor total:'))
         percent= float(input('entre com o valor da porcentagen:'))

    
    
    
    
    
    
    
    
