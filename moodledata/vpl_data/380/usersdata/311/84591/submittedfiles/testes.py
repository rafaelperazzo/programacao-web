a= float(input('Digite seu investimento:'))
t= float(input('Digite sua taxa de lucro:'))
i = a + (a*t)
for i in range (a,11,1):
    i = i + (i*t)
    print('%.2f' %i)
    continue
    