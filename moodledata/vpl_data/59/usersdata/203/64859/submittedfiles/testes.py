C=int(input('capital: '))
i=float(input('taxa: '))
i=i/100
t=int(input('tempo: '))
M=C*(1+i)**t
print('%.2f'% M)