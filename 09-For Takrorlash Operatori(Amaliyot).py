# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:54:58 2022

@author: Dilshod
"""

ismlar = ["Dilshod","Anvar","Ulug'bek","Javlon","Jasur","Javohir"]

#n = 0
#for ism in ismlar:
#    print(f"Assalom-u Alaykum {ism},yaxshi dam oldingizmi?")
#    n = n + 1
#print("Kod",n,"marta takrorlandi!") 

#t_sonlar = list(range(11,100,2))
#for son_kubi in t_sonlar:
#    print(f"{son_kubi} soning kubi:{son_kubi**3}")

#ism = input("Iltimos ismingizni kiriting:")

#print(f"{ism} 5 ta eng yaxshi ko'rgan kinolaringizni kiriting!")
#sev_kino = []
#for kino in range(5):
#    sev_kino.append(input(f"{kino+1}-sevimli kino:"))

#print(f"Sevimli kinolar:\n {sev_kino}")


odam_soni = int(input(f"Bugun nechta odam bilan gaplashdiz ?:"))
odamlar = []

for n in range(odam_soni):
    odamlar.append(input(f"{n+1}-Odam ismi:"))
print("Gaplashgan odamlar ro'yhadi:")   
for odam in odamlar:
    print(">>>",odam)
    





