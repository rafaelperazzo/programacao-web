# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random 
    sort=random.randint(0,2)
    if sort==0:
        return(0)
    if sort==2:
        return(2)
    else:
        return(1)
        
def analise_de_vencedor(tabela):
    if tabela[0][0]==tabela[0][1] and tabela[0][1]==tabela[0][2]:
        return('Venceu')
    elif tabela[1][0]==tabela[1][1] and tabela[1][1]==tabela[1][2]:
        return('Venceu')
    elif tabela[2][0]==tabela[2][1] and tabela[2][1]==tabela[2][2]:
        return('Venceu')
    elif tabela[0][0]==tabela[1][0] and tabela[1][0]==tabela[2][0]:
        return('Venceu')
    elif tabela[0][1]==tabela[1][1] and tabela[1][1]==tabela[2][1]:
        return('Venceu')
    elif tabela[0][2]==tabela[1][2] and tabela[1][2]==tabela[2][2]:
        return('Venceu')
    elif tabela[0][0]==tabela[1][1] and tabela[1][1]==tabela[2][2]:
        return('Venceu')
    elif tabela[2][0]==tabela[1][1] and tabela[1][1]==tabela[0][2]:
        return('Venceu')
    else:
        return('Velha')
        

    