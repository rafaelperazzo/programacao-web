# -*- coding: utf-8 -*-
a=int(input("Digite um número: "))
while a<10000000 or a>99999999:
    print("NAO SEI")
    break
i=0
somo=0
for i in range(10000000,a+1,1):
    i=i+1
print(i)