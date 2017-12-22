notas = []
for i in range (0, 51, 1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
soma=0
for i in range (0, 51, 1):
    soma+= notas[i]
media=soma/50.0
print(notas)
print(media)