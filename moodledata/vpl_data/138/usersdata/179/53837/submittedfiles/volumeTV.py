

 v=int(input('digite o valor de v :'))
 t=int(input('digite o valor de t :'))
 cont=v
 for i in range(1,t+1,1):
    a=int(input('digite a valor de a :'))
    
    if (cont+a)<=100 and cont>=0:
        cont=cont+a
    elif (cont+a)>=100:
        v=cont-100
        cont=cont-v
 print(cont)        
     