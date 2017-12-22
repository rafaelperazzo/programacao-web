print (" BEM-VINDO AO JOGO DA VELHA ")




print("O primeiro jogador será o (X) e o segundo o (O) ")




posicao = """             posicoes do jogo
                 1 | 2 | 3
                -----------
                 4 | 5 | 6
                -----------
                 7 | 8 | 9
          """
print (posicao)
posicoes = [
    (5,7),
    (5,5),
    (5,3),
    (9,7),
    (9,5),
    (9,3),
    (7,7),
    (7,5),
    (7,3),
    ]
ganhador = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
    ]
jogo = []
for vertical in posicao.splitlines():
    jogo.append(list(vertical))
    
jogador = "X"
jogando = True
jogadas = 0

while True:
    for j in jogo:
        print (""".join(t))

