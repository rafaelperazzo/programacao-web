# ENTRADA
n = int(input('ditige o número'))
print('o {:.0f}'.format(n))
n = n//2
print('o valor de {:.0f}'.format( n))

if n//2:
    print('o numero é PAR')
else:
    print('o numero é IMPAR')
print('----FIM----')
