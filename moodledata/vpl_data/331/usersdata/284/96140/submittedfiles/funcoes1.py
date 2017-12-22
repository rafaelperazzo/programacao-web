lista_crescente=[1,2,3]



def crescente(n,lista_crescente):
    cont_crescente=0
    for i in range(0,n-1,1):
        if lista_crescente[i]<lista_crescente[i+1]:
            cont_crescente=cont_crescente+1
    if cont_crescente==len(lista_crescente)-1:
        return('S')
    else:
        return('N')
                break
def decrescente(n,lista_decrescente):
    cont_decrescente=0
    for i in range(0,n-1,1):
        if lista_descrescente[i]>lista_decrescente[i+1]:
            cont_decrescente=cont_decrescente+1
    if cont_decrescente==len(lista_decrescente)-1:
        return('S')
    else:
        return('N')

def consecutivo(n,lista_consecutiva):
    cont_consecutivo=0
    for i in range(0,n-1,1):
        if lista_consecutiva[i]==lista_consecutiva[i+1]:
            cont_consecutivo=cont_consecutivo+1
    if cont_consecutivo>0:
        return('S')
    else:
        return('N')
        
            
            

