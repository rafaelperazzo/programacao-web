# -*- coding: utf-8 -*-
i=1000
while i<=9999:
    dezena1=i%100
    dezena2=i//100
    if (dezena1+dezena2)**2== i:
        print(i)
    i=i+1