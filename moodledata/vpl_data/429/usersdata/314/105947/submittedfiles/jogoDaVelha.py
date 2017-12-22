# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

grupo = 'Breendon, Gustavo, Roberto, Rafael'


print('Bem vindo ao JogodaVelha do grupo {} \n' .format(grupo)) 

continua = 'S'
while continua.upper() == 'S':
    jogar()
    continua = input('Deseja jogar novamente?' )



    
