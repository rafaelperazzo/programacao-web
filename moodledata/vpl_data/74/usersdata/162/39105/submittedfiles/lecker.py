a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))
d=int(input('Digite o quarto número:'))
if (a>b>c>d) and (a<b>c>d) and (a<b<c>d) and (a<b<c<d):
    print('S')    
else:
    print('N')

