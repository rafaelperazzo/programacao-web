# -*- coding: utf-8 -*-
def gangorra():
    p1=float(input("Qual o peso da primeira criança? "))
    c1=float(input("Qual o comprimento da gangorra da primeira criança? "))
    p2=float(input("Qual o peso da segunda criança? "))
    c2=float(input("Qual o comprimento da gangorra da segunda criança? "))
    gan1=p1*c1
    gan2=p2*c2
    if gan1==gan2:
        print "0"
    elif gan1>gan2:
        print "-1"
    elif gan1<gan2:
        print "1"