n=int(input(''))
while n<3:
    n=int(input(''))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
somalinha=[]
for i in range(0,n,1):
    soma=0
    for j in range(0,n,1):
        soma+=matriz[i][j]
    somalinha.append(soma)
somacoluna=[]
for i in range(0,n,1):
    soma=0
    for j in range(0,n,1):
        soma+=matriz[j][i]
    somacoluna.append(soma)
maior=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if (somalinha[i]+somacoluna[j]-(2*matriz[i][j]))>maior:
            maior=(somalinha[i]+somacoluna[j]-(2*matriz[i][j]))
print(maior)