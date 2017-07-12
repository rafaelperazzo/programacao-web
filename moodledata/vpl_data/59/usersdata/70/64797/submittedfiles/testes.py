# -*- coding: utf -8-*
def entraNota(quantidade_nota):
     
     notas = []
     
     int = 1
     for num in range(quantidade_nota):
         
         nota = (float(input("Digite a {0}ª nota: ".format(int))))
         if nota < 0 or nota > 10:
             raise ValueError('Erro na {0}ª nota. Digite uma nota entre 0 e 10.'.format(int))
        notas.append(nota)
        int += 1
    return notas
def mediaAluno(notas):
    soma + sum(notas)
    print(soma)
    media = soma/len(notas)
    
    if media > 7.0 and media < 10:
        print('Aprovado com media:{0}'.format(media))
    elif media <7.0:
        print('Reprovado com media:{0}'.format(media))
    else
        print('Aprovado com 10!')   
notas = entraNotas(3)
mediaAluno(notas)
            