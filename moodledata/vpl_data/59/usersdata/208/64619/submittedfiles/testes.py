# -*- coding: utf-8 -*g
resultado=[]
for i in range(10,100,1):
    for j in range(10,100,1):
        list1=[]
        list2=[]
        k=i*j
        if k<1000 or k>100000:
            continue
        else:
            for item in str(i):
                list1.append(item)
            for item in str(j):
                list1.append(item)
            for item in str(k):
                list2.append(item)
            cont=1
            for carta in list1:
                if carta not in list2:
                    cont=0
                else:
                    list2.remove(carta)
            for carta in list2:
                if carta not in list1:
                    cont=0
            if cont==1:
                if k not in resultado:
                    resultado.append(k)
for carta in resultado:
    print(carta)
                
               
#como o trabalho pede apenas os numeros vampiros de quatro digitos 
#definindo os dois intervalo de 10 à 100 para encontramos
#os números vampiros de 4 digitos, se definimos os intervalos de 10 a 100 
#encontramos outros numeros vampiros.O programa está basicamente multiplicando 
#os intervalos e depois jogando o resultado na lista2,e criando uma lista1 
#pegando os valores de i e j,depois que ja tem a lista1 e lista2 ele cont=1
#logo em seguida ele verifica se os elementos da lista1 estão dentro da lista2
#se não estiver, os elementos da lista1 é removido,