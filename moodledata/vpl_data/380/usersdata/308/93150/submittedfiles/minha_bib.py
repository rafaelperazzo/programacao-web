# -*- coding: utf-8 -*-
def testeum():
    a = 10
    print(id(a))
def testedois():
    a = 10
    print(id(a))

def porextenso(x):
    unidade = ['', ' e um', ' e dois', ' e tres',' e quatro', ' e cinco', ' e seis', ' e sete', ' e oito', ' e nove']
    dezena = ['', ' e dez', ' e vinte', ' e trinta',' e quarenta', ' e cinquenta', ' e sessenta', ' e setenta',  ' e oitenta', ' e noventa']
    centena = ['', 'Cento', 'Duzentos', 'Trezentos','Quatrocentos', 'Quinhentos', 'Seiscentos', 'Setecentos', 'Oitocentos', 'Novecentos']
    
    return (centena[int(x[0])] + dezena[int(x[1])] + unidade[int(x[2])])