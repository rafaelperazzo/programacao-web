# -*- coding: utf-8 -*-
def testeum():
    a = 10
    print(id(a))
def testedois():
    a = 10
    print(id(a))

def porextenso(x):
    unidade = ['', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezena = ['', 'dez', 'vinte', 'trinta','quarenta', 'cinquenta', 'sessenta', 'setenta',  'oitenta', 'noventa']
    centena = ['', 'Cento', 'duzentos', 'trezentos','quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
    
    return (unidade[int(x[0])]+' '+dezena[int(x[1])] + ' '+centena[int(x[2])])