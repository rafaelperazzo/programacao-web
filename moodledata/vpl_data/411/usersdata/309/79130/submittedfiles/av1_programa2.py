# -*- coding: utf-8 -*-
pre=float(input ("Valor de etiqueta:"))
opc=int(input("Opção de pagamento:"))


if opc==1:
    b=pre - (pre*(0.15))
    print("%.2f" %b)
elif opc==2:
    b=pre - (pre*(0.10))
    print("%.2f" %b)
elif opc==3:
    b=pre
    print("%.2f" %b)
elif opc==4:
    b=pre*(1.10)
    print("%.2f" %b) 

else:
    print("A opção de pagamento digitada, não existe.")
    
