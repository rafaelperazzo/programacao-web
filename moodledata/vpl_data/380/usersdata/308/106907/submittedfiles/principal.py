def converterBinario(valor):
    resultado=''
    while valor>2:
        if valor%2==0:
            resultado += '1'
        else:
            resultado += '0'
        valor = valor/2
    return resultado
a = 4
print(converterBinario(a))