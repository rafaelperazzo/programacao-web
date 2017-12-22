"""
EE2: Escreva um programa em Python que cria uma matriz m x n 
     preenchida com zeros e mostra a matriz na tela
"""

# Funcao de criar a matriz
def cria_matriz(m,n,valor_inicial) :
	matriz = []
	for i in range(m):
		linha = []
		for j in range(n):
			linha.append(valor_inicial)
		matriz.append(linha)
	return matriz

# Funcao que faz as acoes do programa principal
def main() :
	# le do usuario as dimensoes da matriz
	m = int(input('Digite a dimensão m (linhas) da matriz: '))
	n = int(input('Digite a dimensão n (colunas) da matriz: '))
	matriz = cria_matriz(m,n,0)
	print(matriz)
	return

# Programa Principal
main()