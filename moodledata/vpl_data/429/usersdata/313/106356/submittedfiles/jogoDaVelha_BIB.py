nome_do_jogador= ''
simbolo_do_jogador= ''
simbolo_do_pc= ''



tabuleiro="""               Posições
  |  |        00|01|02   
  |  |        10|11|12
  |  |        20|21|22
  """
posicoes= [
    (0,0),
    (0,1),
    (0,2),
    (1,0),
    (1,1),
    (1,2),
    (2,0),
    (2,1),
    (2,2),
    ]
Vencedor= [
    [00, 01, 02],
    [10, 11, 12],
    [20, 21, 22],
    [00, 10, 20],
    [01, 11, 21],
    [02, 12, 22],
    [00, 11, 22],
    [20, 11, 02],
    ]
matriz=[]
def mostraTabuleiro():
    for linha in tabuleiro.splitlines():
    matriz.append(list(linha))

    
    
