n= int(input('Ordem da matriz: '))
a=[i,j]

for i in range(n):
    a.append(int(input('Insira valor: ')))
    for j in range(n):
        a.append(int(input('Insira valor: ')))
print(a)