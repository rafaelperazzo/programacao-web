a = float(input('Que horas são'))
if a > 3 and a < 12:
    
    print('bom dia')
elif a >= 12 and a < 18:
    
    print('boa tarde')
    
elif a>= 18 and a <23:
    print('boa noite')

else:
    print('hora inválida')