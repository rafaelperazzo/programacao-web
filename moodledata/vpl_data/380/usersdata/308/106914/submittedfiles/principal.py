def converterBinario(valor):
    resultado=''
    while valor>1:
        resultado += str(valor%2)
        valor = valor//2
    resultado +='1'
    return resultado[::-1]

a = int(input('Informe o valor: '))
print(converterBinario(a))