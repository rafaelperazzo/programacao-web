f=float(input('digite o valor de f:'))
l=float(input('digite o valor de l:'))
q=float(input('digite o valor de q:'))
deltaH=float(input('digite o valor de deltaH:'))
V=float(input('digite o valor de v:'))
d=((8*f*l*q**2)/(3.14**2)*9.81*deltaH)**1/5
rey=((4*q)/(3.14*d*v))
k=(0.25/((math.log10)(0.000002/3.7*d)+(5.74/rey**0.9)))**2
print('%.4f'%d)
print('%.4f'%rey)
print('%.4f'%k)
