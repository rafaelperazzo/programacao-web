# -*- coding: utf-8 -*-
n=float(input('Digite o valor do produto: '))
opçao=string(input('Digite a opçao de pagamento entre opçao1,opçao2,opçao3 e opçao4: '))
opçao1=n-(n*(15/100))
opçao2=n-(n*(10/100))
opçao3=n
opçao4=n+(n*(10/100))
if opçao1 or opçao2 :
    print('{:.2f} {:.2f}'.format(opçao1,opçao2))
elif opçao2:
    print('{:.2f}'.format(opçao2))
elif opçao3:
    print('{:.2f}'.format(opçao3))
elif opçao4:
    print('{:.2f}'.format(opçao4))
    