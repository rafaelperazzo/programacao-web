def converterBinario(valor):
    resultado=''
    while valor>1:
        if valor%2==1:
            resultado.append('1')
        else:
            resultado.append('0')
        valor = valor/2
    return resultado
a = 4
print(converterBinario(a))