# 1. Ler uma matriz m,n de inteiros
while(True):
    n = int(input('Digite a quantidade de linhas e colunas: '))
    if n >= 1 and n <= 100:
        break
    else:
        print('Numero invalido. Digite entre 1 e 100 (inclusive)')

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input('Digite uma distancia: ')))
    matriz.append(linha)

# 2. Receber um intinerario a percorrer
#    - uma lista de inteiros
while(True):
    c = int(input('Digite a quantidade de cidades do percurso: '))
    if c >= 2 and c <= 100:
        break
    else:
        print('Numero invalido. Digite entre 2 e 100 (inclusive)')

percurso = []
for i in range(c):
    while(True):
        ci = int(input('Digite uma cidade: '))
        if ci >= 0 and ci < n:
            break
        else:
            print('Cidade invalida. Digite entre 0 e %d (inclusive)' % (n-1))
    percurso.append(ci)

# 3. Calcular o custo do trajeto 
custo = 0
for i in range(0,c-1,1):
    custo = custo + matriz[percurso[i]][percurso[i+1]]

print(custo)













