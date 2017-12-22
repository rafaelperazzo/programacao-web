n= int(input('Ordem da matriz: '))
a=[]
b= []

for i in range(n**2):
    a.append(int(input('Insira valor: ')))
    for j in range(n**2):
        b.append(int(input('Insira valor: ')))
print(a)