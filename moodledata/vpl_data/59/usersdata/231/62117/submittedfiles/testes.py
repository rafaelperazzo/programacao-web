
    
# Como já se sabe,só existem sete números vampiros de quatro digitos,sendo que
# quatro deles atendem a mesma condição de permutação para que sejam vampiros,onde
# tal condição é que, inverte o indice[0] com o indice[1] , e o indice[2] e o indice[3]
# permanecem no mesmo lugar, e com isso faz a multiplicação da soma de ambos,so que em forma
# de texto ultilizando para essa transformação a função (str), e depois retornando o
# valor dessa soma para um número natural inteiro com a função
# (int), fazendo também esse mesmo processo para o número( se é vampiro ou não) dado,
# para poder fazer a comparação de igualdade, entre o número dado e a multiplicação
# entre as permutações, pois se ambos forem iguais o número será vampiro, se não,
# não será vampiro. Faz-se o mesmo para as outras condições onde inverte-se o indice[2]
# com o indice[1] e faz a soma de ambos e depois a multiplição dessa soma pela a soma
# do indice[0] + o indice[3], e a última condição é que, inverte o indice[2] com o indice[0]
# faz a soma, e multiplica por a soma do indice[1] +  indice[3], logo todos os números vampiros
# atenderam a essas condições.
 

    
def max(a,b):
    if a>b:
        return a
    else:
        return b
a=2
b=3
print (max(a,b))
        
    
