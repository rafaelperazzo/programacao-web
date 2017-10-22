n = float(input('Valor do investimento inicial:'))
t = float(input('taxa de crescimento percentual:'))
e=1
while e<11:
    vf=n*((1+t)**e)
    print (vf)
    e=e+1




