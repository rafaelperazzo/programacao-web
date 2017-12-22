
m = int(input('quant de colunas'))
n = int(input('quant de linhas'))
matriz = []

for i in range(1,m+1,1):
    l = []
    for j in range (0,n+1,1):
        l.append(input('digite um valor'))
    matriz.append(l)
for i in range (0,m,1):
    for j in range (0,n,1):
        if matriz[i][j]>10:
            print(matriz[i][j])
    
    

    
