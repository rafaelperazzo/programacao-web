n=int(input('Número de notas:'))
notas = []
media=0
for i in range(0,n,1):
    media+=notas[i]/n
for i in range (0,n,1):
    print(notas[i])
    