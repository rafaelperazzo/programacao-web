"""
EE1: Calcule a média da turma!
"""
# inicializa a matriz de notas da turma
turma = [
    [5.0, 4.5, 7.0, 5.2, 6.1], 
    [2.1, 6.5, 8.0, 7.0, 6.7], 
    [8.6, 7.0, 9.1, 8.7, 9.3]
]
# descobre o tamanho da turma
linhas = size(turma)
colunas = size(turma[0])
# inicializa a variavel de calculo da media
media = 0
# laco de repeticao para percorrer as linhas
for i in range(linha):
	# laco de repeticao para percorrer as colunas
	for j in range(colunas):
		media = media + turma[i][j]
# finaliza calculo da media
media = media / (linhas * colunas)
# exibe na tela o resultado
print(media)