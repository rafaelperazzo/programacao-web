a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))
if a > 0 and b > 0 and c > 0:
    if a == c and c == b:
        print('triângulo Equilátero')
    if a == b and a != c:
        print('triangulo isósceles')
    if b == c and b != a:
        print('triangulo isósceles')
    if a != b and b != c:
        print('triangulo escaleno')
else:
    print('isso não é um triângulo')