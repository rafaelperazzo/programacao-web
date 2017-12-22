notas = []
for i in range (0, 51, 1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))
media = 0
for i in range (0, 51, 1):
    soma+= notas[i]
media=soma/5.0
print(notas)
print(media)