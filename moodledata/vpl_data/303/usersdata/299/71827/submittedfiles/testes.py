a=int(input('Que horas são? [0-23]'))
while a<0 or a>23:
    print('Hora inválida')
    a=int(input('Que horas são? [0-23]'))
else:
    if a>3 and a<12:
        
        print('Bom dia')
     
    elif a>=12 and a<18:
        print('Boa tarde')
    else:
        print('boa noite')