n = int(input('Digite a quantidade de notas: '))
while n<=1:
    n = int(input('Digite a quantidade de notas: '))

notas = []
for i in range (0, n, 1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
soma=0
for i in range (0, n, 1):
    soma+= notas[i]
media=soma/float(n)
print(notas)
print(media)