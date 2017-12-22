q = int(input("Digite a quantidade de notas: "))
notas = [q]
for i in range (0,q,1):
    notas.append(float(input("Digite a nota%d: " %(i+1))))
media = 0
for i in range (0,q,1):
    media+=notas[i]/q
print(notas)
print(media)