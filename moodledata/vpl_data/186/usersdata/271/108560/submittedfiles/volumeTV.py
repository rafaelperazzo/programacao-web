
v = int(input('Digite o volume inicial : '))
y = int(input('Digite a quantidade de mudanças : '))
a = []
for i in range(0,y,1) :
    vol = int(input('Digite o volume : '))
    a.append(vol)
soma = v
for i in range(0,y,1) :
    soma = soma + a[i]
    if (soma>=100) :
        soma = 100
print(soma)