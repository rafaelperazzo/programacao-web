from minha_bib import*
import random
num_participantes=22
participantes=['Monteiro', 'Florinda', 'Neidjane', 'Neidje-Ieb Neto', 'Alane', 'Fátima', 'Rafaela', 'Gustavo', 'Tatiane', 'Luiz', 'Felipe', 'Denise', 'Thiago', 'Nertan', 'Patrícia', 'Gabriel', 'Rafael', 'Ney', 'Adriana', 'Pedro Lucas', 'Marcos Vinícius', 'Dona Geísa', 'Seu Pedrosa']
for i in range (0,22,1):
    sorteio=random.randint(0,num_participantes-1)
    print(participantes[sorteio])
    del participantes[sorteio]