a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
#Para o maior
if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > b:
    print(c)
#Caso alguns sejam iguais
if a == b and a > c:
    print(a)
if b == a and b > c:
    print(b)
if a == c and a > b:
    print(a)
if b == c and b > a:
    print(b)
if a == c and c > b:
    print(c)
if b == c and c > a:
    print(c)
