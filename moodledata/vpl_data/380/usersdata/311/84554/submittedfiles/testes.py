a= float(input('Digite seu investimento:'))
t= float(input('Digite sua taxa de lucro:'))
for i in range (a,11,t):
    a=a+(a*t)
    print (i)
    