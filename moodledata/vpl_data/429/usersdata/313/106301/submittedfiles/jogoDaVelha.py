
class jogadainvalida(Exception):pass
def mostraTabuleiro(m):
    tabuleiro= """
    ----------------| %s | %s | %s |
    ----------------| %s | %s | %s |
    ----------------| %s | %s | %s |
    ----------------
    """ %([0][0],[0][1],[0][2],[1][0],[1][1],[1][2],[2][0],[2][1],[2][2])
    linha1=[' ',' ',' ']
    linha2=[' ',' ',' ']
    linha3=[' ',' ',' ']
    matriz=[linha1,linha2,linha3]
mostraTabuleiro(m)