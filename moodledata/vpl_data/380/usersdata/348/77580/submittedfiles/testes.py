ns = int(input( ' informe o numero: '))

#calcular o 20
if ns >= 20:
    x1 = ns//20
    ns -= x1*20
    print('%.d' %x1)
else:
    print(0)
    
#calcular 10
if ns>= 10:
    x1 = ns//10
    ns -= ns*10
    print('%.d' %x1)
else:
    print(0)

#calcular 5
if  ns >= 5:
    x1 = ns//5
    ns -= x1*5
    print('%.d' %x1)
else:
    print(0)
    
#calcular 2
if (ns>= 2):
    x1 = ns//2
    ns -= x1*2
    print('%.d' %x1)
else:
    print(0)
    
#calcular 1 
if ns>= 1:
    x1 = ns//1
    ns -= x1
    print('%d' %x1)
else:
    print(0)

    
































