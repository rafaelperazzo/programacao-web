p1=float(input('Digite o peso da criança do lado esquerdo:'))
p2=float(input('Digite o peso da criança do lado direito:'))
c1=float(input('Digite o comprimento da gangorra do lado esquerdo:'))
c2=float(input('Digite o comprimento da gangorra do lado direito:'))
if (p1*c1>p2*c2):
    print('menos um')
elif (p1*c1<p2*c2):
    print('um')
else:
    print('zero')

