# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
ap1= int(input(' '))
ap2= int(input(' '))
ap3= int(input(' '))
ap4= int(input(' '))
ap5= int(input(' '))
ap6= int(input(' '))
sot1= int(input(' '))
sot2= int(input(' '))
sot3= int(input(' '))
sot4= int(input(' '))
sot5= int(input(' '))
sot6= int(input(' '))
if ap1==sot1 or ap1==sot2 or ap1==sot3 or ap1==sot4 or ap1==sot5 or ap1==sot6 :
    if ap2==sot1 or ap2==sot2 or ap2==sot3 or ap2==sot4 or ap2==sot5 or ap2==sot6 :
        if ap3==sot1 or ap3==sot2 or ap3==sot3 or ap3==sot4 or ap3==sot5 or ap3==sot6 :
            if ap4==sot1 or ap4==sot2 or ap4==sot3 or ap4==sot4 or ap4==sot5 or ap4==sot6 :
                if ap5==sot1 or ap5==sot2 or ap5==sot3 or ap5==sot4 or ap5==sot5 or ap6==sot6 :
                    if ap6==sot1 or ap6==sot2 or ap6==sot3 or ap6==sot4 or ap6==sot5 ap6==sot6 :
                        print("sena")
                    else :
                        print("quina")
                else :
                    print("quadra")
            else :
                print("terno")
        else :
            print("azar")
    else :
        print("azar")
else:
    print("azar")