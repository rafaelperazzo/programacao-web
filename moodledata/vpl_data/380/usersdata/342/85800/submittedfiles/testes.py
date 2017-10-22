t1 = int(input('Número de tomadas da régua 01:'))
t2 = int(input('Número de tomadas da régua 02:'))
t3 = int(input('Número de tomadas da régua 03:'))
t4 = int(input('Número de tomadas da régua 04:'))

vf1 = t1 - 1
vf2 = t2 - 1
vf3 = t3 - 1

while (t1 or t2 or t3 or t4) < 1:
    print ("insira um valor maior que 1")
print (vf1+vf2+vf3+t4)

