# -*- coding: utf-8 -*-
n=float(input('Digite o valor do produto: '))
opçao=str(input('Digite a opçao de pagamento entre opçao1,opçao2,opçao3 e opçao4: '))
opçao1=n-(n*(15/100))
opçao2=n-(n*(10/100))
opçao3=n
opçao4=n+(n*(10/100))
if opçao1 :
    print('{:.2f} {:.2f}'.format(opçao1,))
else:    
    elif opçao2:
        print('{:.2f}'.format(opçao2))
        else:
            elif opçao3:
                print('{:.2f}'.format(opçao3))
            else:
                elif opçao4:
                    print('{:.2f}'.format(opçao4))
    