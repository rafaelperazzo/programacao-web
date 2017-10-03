x=float(input('num: '))
if x>=0:
    math.sqrt(x)
    print(x)
    
elif x<0:
    x=x**2
    print('%.2f'%x)
