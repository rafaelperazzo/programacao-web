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

# 2. Receber um intinerario a percorrer
#    - uma lista de inteiros
# 3. Calcular o custo do trajeto informado