# -*- coding: utf-8 -*-
na1=int(input('digite o primeiro numero apostado:'))
na2=int(input('digite o segundo numero apostado:'))
na3=int(input('digite o terceiro numero apostado:'))
na4=int(input('digite o quarto numero apostado:'))
na5=int(input('digite o quinto numero apostado:'))
na6=int(input('digite o sexto numero apostado:'))
ns1=int(input('digite o primeiro numero sorteado:'))
ns2=int(input('digite o segundo numero sorteado:'))
ns3=int(input('digite o terceiro numero sorteado:'))
ns4=int(input('digite o quarto numero sorteado:'))
ns5=int(input('digite o quinto numero sorteado:'))
ns6=int(input('digite o sexto numero sorteado:'))
cont=0
if (na1==ns1 or na1==ns2 or na1==ns3 or na1==ns4 or na1==ns5 or na1==ns6): 
    cont=cont+1
elif (na2==ns1 or na2==ns2 or na2==ns3 or na2==ns4 or na2==ns5 or na2==ns6): 
    cont=cont+1
elif (na3==ns1 or na3==ns2 or na3==ns3 or na3==ns4 or na3==ns5 or na3==ns6):
    cont=cont+1
    print ('terno')
elif (na4==ns1 or na4==ns2 or na4==ns3 or na4==ns4 or na4==ns5 or na4==ns6):
    cont=cont+1
elif (na5==ns1 or na5==ns2 or na5==ns3 or na5==ns4 or na5==ns5 or na5==ns6):
    cont=cont+1
elif (na6==ns1 or na6==ns2 or na6==ns3 or na6==ns4 or na6==ns5 or na6==ns6):
    cont=cont+1
    
if cont==3:
        print ('terno')
if cont==4:
        print ('quadra')
if cont==5:
        print('quina')
elif cont<3:
        ('azar')    
    
