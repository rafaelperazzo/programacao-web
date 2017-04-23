# -*- coding: utf-8 -*-
import math
cv = int(input("Quantas vitórias o Cormengo teve? "))
ce = int(input("Quantos empates o Cormengo teve? "))
cs = int(input("Qual o saldo de gols do Cormengo teve? ")
fv = int(input("Quantas vitórias o Flaminthians teve? "))
fe = int(input("Quantos empates o Flaminthians teve? "))
fs = int(input("Qual o saldo de gols do Flaminthians teve? ")

pontc = (cv*3)+(ce)
pontf = (fv*3)+(fe)

if (pontc>pontf):
    print "C"
elif (pontf>pontc):
    print "F"
elif (pontf==pontc) and (cs>fs):
    print "C"
elif (pontf==pontc) and (fs>cs):
    print "F"
elif (pontf==pontc) and (cs==fs):
    print "="
    