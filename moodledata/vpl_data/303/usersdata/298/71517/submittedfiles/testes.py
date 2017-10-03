print('Sejam a, b e c os coeficientes reais de uma equação do segundo grau.')
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
delta = float(b**2 - (4*a*c))
if delta>=0:
    x1 = round(float((-b/2*a) + (delta**(0.5))/(2*a)), 2)
    x2 = round(float((-b/2*a) - (delta**(0.5))/(2*a)), 2)
    print(x1)
    print(x2)
else:
    print('SRR')



valor = int(input('Digite o valor que deseja sacar: '))

notas20 = int(valor//20)
resto20 = int(valor%20)

notas10 = int(resto20//10)
resto10 = int(resto20%10)

notas5 = int(resto10//5)
resto5 = int(resto10%5)

notas2 = int(resto5//2)
resto2 = int(resto5%2)

notas1 = int(resto2//1)

print(notas20)
print(notas10)
print(notas5)
print(notas2)
print(notas1)