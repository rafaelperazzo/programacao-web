raio = float(input('Insira o raio do círculo, em centímetros: '))
area = float(raio*(3.141592)*2)
print('A área do círculo é, em centímetros quadrados, A=%.2f' % area)

altura = float(input('Qual a sua altura, em metros?: '))
peso = float((72.7*altura) - 58)
print('Seu peso ideal é %.2f' % peso)

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