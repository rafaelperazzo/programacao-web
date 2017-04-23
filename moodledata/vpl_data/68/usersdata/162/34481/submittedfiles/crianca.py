p1=float(input('Digite o peso1:'))
c1=float(input('Digite o comprimento1:'))
p2=float(input('Digite o peso2:'))
c2=float(input('Digite o comprimento2:'))
if (p1*c1==p2*c2):
    print('0')
if (p1*c1>p2*c2):
    print('-1')
if (p1*c1<p2*c2):
    print('1')

