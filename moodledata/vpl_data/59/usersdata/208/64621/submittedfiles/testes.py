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
            for elementos in list1:
                if elementos not in list2:
                    cont=0
                else:
                    list2.remove(elementos)
            for elementos in list2:
                if elementos not in list1:
                    cont=0
            if cont==1:
                if k not in resultado:
                    resultado.append(k)
for elementos in resultado:
    print(elementos)
                
               
#como o trabalho pede apenas os numeros vampiros de quatro digitos 
#definindo os dois intervalo de 10 à 100 para encontramos
#os números vampiros de 4 digitos, se definimos os intervalos de 10 a 100 
#encontramos outros numeros vampiros.O programa está basicamente multiplicando 
#os intervalos e depois jogando o resultado na lista2,e criando uma lista1 
#pegando os valores de i e j,depois que ja tem a lista1 e lista2 ele cont=1
#logo em seguida ele verifica se os elementos da lista1 estão dentro da lista2
#se não estiver cont=0, se tiver ele reseta a lista2, depois faz esse processo
#na lista2.Por fim se cont=1 ele não vai pegar 