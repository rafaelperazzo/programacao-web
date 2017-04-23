P1=float(input('Digite o peso da criança 1:'))
C1=float(input('Digite o comprimento 1: '))
P2=float(input('Digite o peso da criança 2: '))
C2=float(input('Digite o comprimento 2: '))

fator1=P1*C1
fator2=P2*C2

if fator1==fator2:
    print('zero')
    
if fator1>fator2:
    print ('menos um')
    
if fator1<fator2:
    print('um')