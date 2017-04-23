p1=int(input('Digite o peso da criança do lado esquerdo:'))
p2=int(input('Digite o peso da criança do lado direito:'))
c1=int(input('Digite o comprimento da gangorra do lado esquerdo:'))
c2=int(input('Digite o comprimento da gangorra do lado direito:'))
if (p1*c1==p2*c2):
    print('0')
if (p1*c1>p2*c2):
    print('-1')
if (p1*c1<p2*c2):
    print('1')

