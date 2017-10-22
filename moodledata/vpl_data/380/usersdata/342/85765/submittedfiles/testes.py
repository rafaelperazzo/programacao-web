n = float(input('Valor do investimento inicial:'))
t = float(input('taxa de crescimento percentual:'))
e=1
while e<11:
    valorfinal = n*((1+t)**e)
    print ("%.2f" %valorfinal)
    e=e+1




