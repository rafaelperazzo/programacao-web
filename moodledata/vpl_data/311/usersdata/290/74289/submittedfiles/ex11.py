# -*- coding: utf-8 -*-
d1=int(input("Digite o dia1: "))
m1=int(input("Digite o mês1: "))
a1=int(input("Digite o ano1: "))
d2=int(input("Digite o dia2: "))
m2=int(input("Digite o mês2: "))
a2=int(input("Digite o ano2: "))
if a2>a1:
    print("DATA2")
elif a2<a1:
    print("DATA1")
elif a1==a2 and m2>m1:
    print("DATA2")
elif a1==a2 and m2<m1:
    print("DATA1")
elif a1==a2 and m2=m1 and d2>d1:
    print("DATA2")
elif a1==a2 and m2=m1 and d2<d1:
    print("DATA1")
elif a1==a2 and m2=m1 and d2=d1: 
    print("IGUAIS")






    


    



