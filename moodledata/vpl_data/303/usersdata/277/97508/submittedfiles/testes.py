"""
EE3: Escreva um programa em Python que armazena os nomes e idades de 
     6 pessoas em uma matriz, e imprime o nome da pessoa mais nova.
"""
matriz = []
# preenche a matriz
for i in range(6):
	linha = []
	linha.append(input('Digite o nome da pessoa '+str(i)+':'))
	linha.append(int(input('Digite a idade de '+linha[0]+':')))
	matriz.append(linha)
# procura a pessoa mais nova
menor = matriz[0][1]	# inicia menor com a idade da primeira pessoa
pos = 0					# inicia posicao do menor na matriz
for i in range(6):
	if matriz[i][1] < menor:
		menor = matriz[i][1]
		pos = i
# imprime a matriz
for i in range(6):
	print(matriz[i])
# imprime o nome da pessoa mais nova	
print('A pessoa mais nova eh: ' + matriz[pos][0])