d = float(input('d: '))
if (d>0)
    print('d é maior que zero')
else
    print('d é menor que zero')


n1 = float(input('Digite um valor N1: '))
n2 = float(input('Digite um valor N2: '))
n3 = float(input('Digite um valor N3: '))
total = n1 + n2 + n3
print('TOTAL = %f' % total)

print('\n')
raio = float(input('Insira o raio do círculo, em centímetros: '))
pi = 3.141592
area = float(pi*((raio)**2))
print('A área do círculo é, aproximadamente, A=%.3f cm^2' % area)

print('\n')
altura = float(input('Qual a sua altura, em metros?: '))
peso = float((72.7*altura) - 58)
print('Seu peso ideal é %.2f kg' % peso)

print('\n')
metro = float(input('Insira a medida f, em metros: '))
cent = float((metro)*100)
print('A medida f é f=%.2f cm' % cent)

print('\n')
nota1 = float(input('Qual sua primeira nota?: '))
nota2 = float(input('Qual sua segunda nota?: '))
nota3 = float(input('Qual sua terceira nota?: '))
nota4 = float(input('Qual sua quarta nota?: '))
media = float((nota1 + nota2 + nota3 + nota4)/4)
print('Sua média é %.1f' % media)