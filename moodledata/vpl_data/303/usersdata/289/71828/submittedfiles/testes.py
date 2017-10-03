a = int(input('Que horas são? [0-23]'))
if a < 0 or a > 23:
    print('hora invalida')
else:
    if a > 3 and a < 12 :
         print('bom dia')
    elif a>=12 and a<18 :
        print('boa tarde')
    else:
        print(' boa noite')
