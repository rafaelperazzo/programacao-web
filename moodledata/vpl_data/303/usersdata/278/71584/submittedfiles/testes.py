print('Olá!!')
print('\n')
a = input('Que horas são? [0-23] ')
if a > 3 and a < 12:
    print('Bom dia')
elif a >= 12 and a < 18:
    print('Boa tarde')
else:
    print('Boa noite')