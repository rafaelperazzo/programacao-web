lista_crescente=[6,5,4]


def crescente(n,lista_crescente):
    cont_crescente=0
    for i in range(0,n-1,1):
        if lista_crescente[i]<lista_crescente[i+1]:
            cont_crescente=cont_crescente+1
    if cont_crescente==len(lista_crescente)-1:
        return('S')
    else:
        return('N')

def decrescente(n,lista_decrescente):
    cont_decrescente=0
    for i in range(0,n-1,1):
        if lista_descrescente[i]>lista decrescente[i+1]:
            cont_decrescente=cont_decrescente+1
    if cont_decrescente==len(lista_decrescente)-1:
        return('S')
    else:
        return('N')
        
            
            

