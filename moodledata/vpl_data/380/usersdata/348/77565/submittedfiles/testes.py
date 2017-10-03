
print (type('x')) 






























'''
a = float(input('informe a: '))
b = float(input('informe b: '))
c = float(input('informe c: '))
a1 = float(input("informe a': "))
b1 = float(input("informe b': "))

b = b - a1
c = c - b1
try:
    delta = (b**2) - (4*a*c)
    x1 = (-b + ((delta)**(0.5)))/(2*a)
    x2 = (-b - ((delta)**(0.5)))/(2*a)
    print('%.2f' %x1)
    print('%.2f' %x2)
except:
    print('Impossível')
finally:
    print('pronto')

