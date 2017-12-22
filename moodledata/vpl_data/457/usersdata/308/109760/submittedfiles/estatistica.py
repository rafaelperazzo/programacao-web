def calculaMedia(lista):
  x = sum(lista)/len(lista)
  return x

def calculaDesvio(lista):
  media = calculaMedia(lista)
  for i in range (len(lista)):
    lista[i] = ((lista[i]-media)**2)/(len(lista)-1)
  desvioPadrao = (sum(lista))**(0.5)
  return desvioPadrao
  

#Informe a quantidade de listas 
qnt = int(input(''))
#Informe a quantidade de elementos
qnt2 = int(input(''))

matriz = []
for i in range (qnt):
  matriz.append([])
  for j in range(qnt2):
    matriz[i].append(int(input('Lista %d item %d: ' % (i, j))))

for i in range(qnt):
  print('%.2f' % (calculaMedia(matriz[i])))
  print('%.2f' % (calculaDesvio(matriz[i])))