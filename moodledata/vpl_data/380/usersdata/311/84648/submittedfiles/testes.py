a= int(input('Digite seu investimento:'))
t= float(input('Digite sua taxa de lucro:'))

for a in range (a,a+10,2):
    a = a + (a*t)
    print('%.2f' %a)
    continue
    