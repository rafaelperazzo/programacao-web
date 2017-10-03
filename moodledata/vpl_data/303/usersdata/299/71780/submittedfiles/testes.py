a=int(input('Que horas são? [0-23]'))
if a>3 and a<12:
    print('Bom dia')
elif a>=12 and a<18:
    print('Boa tarde')
elif a>=18 and a<=23:
    print('Boa noite')
elif a<0 or a>23:
    print('Hora inválida')
    