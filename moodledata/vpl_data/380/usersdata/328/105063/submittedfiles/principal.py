a = input('Digite a: ')

b = input('Digite b:')

q = input('Digite q: ')

c = 0

i = 2

while i<=q:

    if a%i==0 and b%i==0:

        c = c + i

    i = i + 1

print (c)