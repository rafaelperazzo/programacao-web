print('Olá!!')
print('\n')
a = int(input('Que horas são? [0-23] '))
if a<0 and a>23:
    print('erro')
if a>3 and a<12:
    print('\n-------------------------')
    print('Bom dia')
elif a>=12 and a<18:
    print('Boa tarde')
elif a>=18:
    print('Boa noite')