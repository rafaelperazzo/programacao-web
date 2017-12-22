def converterBinario(valor):
    resultado=''
    while valor>1:
        resultado += str(valor%2)
        valor = valor//2
    resultado +='1'
    return resultado[::-1]
a = 4
print(converterBinario(a))