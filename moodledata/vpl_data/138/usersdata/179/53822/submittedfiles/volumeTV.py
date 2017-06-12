

 v=int(input('digite o valor inicial do volume :'))
 t=int(input('digite o valor de trocas do volume :'))
 cont=v
 for i in range(1,t+1,1):
    tr=int(input('digite as trocas de volumes :'))
    if (cont +tr)<=100 and cont>=0:
        cont=cont+tr
    elif cont+tr>=100:
        v=cont-100
        cont=cont-v
print(cont)        
     