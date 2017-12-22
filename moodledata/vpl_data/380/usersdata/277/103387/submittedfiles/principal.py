# 1. Ler uma matriz m,n de inteiros
while(True):
    m = int(input('Digite a quantidade de linhas: '))
    if m >= 1 and m <= 100:
        break
    else:
        print('Numero invalido. Digite entre 1 e 100 (inclusive)')

while(True):
    n = int(input('Digite a quantidade de colunas: '))
    if n >= 1 and n <= 100:
        break
    else:
        print('Numero invalido. Digite entre 1 e 100 (inclusive)')

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(int(input('Digite uma distancia: ')))
    matriz.append(linha)

# 2. Receber um intinerario a percorrer
while(True):
    c = int(input('Digite a quantidade de cidades do percurso: '))
    if c >= 2 and c <= 100:
        break
    else:
        print('Numero invalido. Digite entre 2 e 100 (inclusive)')

percurso = []
for i in range(c):
    percurso.append(int(input('Digite uma cidade: ')))









#    - uma lista de inteiros
# 3. Calcular o custo do trajeto 













