import math
f = float(input('digite o valor f:'))
L = float(input('digite o valor L:'))
Q = float(input('digite o valor Q:'))
deltaH = float(input('digite o valor deltaH:'))
v = float(input('digite o valor v:'))
g = 9.81
e = 0.000002
D = (8*f*L*Q**2)/g*deltaH*(math.pi**2)**(1/5)
Rey = 4*Q/math.pi*D*v
k = 0.25/(math.log10(e/3.7*D+(5.74/Rey**0.9)))**2
print('D=%.4f'%D)
print('Rey=%.4f'%Rey)
print('k=%.4f'%k)