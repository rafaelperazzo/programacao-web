print('Sejam a, b e c os coeficientes reais da equação do segundo grau ax^2 +bx +c = 0.')
a = (input('Digite a: '))
b = (input('Digite b: '))
c = (input('Digite c: '))
d = (b*b - (4*a*c))
if d>=0
    delt = d**(1/2)
elif d<0
    delt = (-d)**(1/2)*j 
x1 = ((-b + delt)/2)
x2 = ((-b - delt)/2)
print('A variável x assume os valores x1=% e x2=%' % (x1, x2)) 

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