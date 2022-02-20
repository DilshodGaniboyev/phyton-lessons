# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:04:38 2022

@author: Dilshod
"""

buyurtmalar = []

e_bozor = {'non':1500,'un':1800,'lag\'mon':13000,'guruch':18000,'sabzi':10000}

while True:
     buyurtmalar.append(input("Nima buyurtma qilasiz?\n>>>"))
     sorov = input("Yana buyurtma qilasizmi?(Ha/Yo'q):")
     if sorov=="Yo'q":
         break
     else :
         continue
     
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in e_bozor.keys():
        narx = e_bozor[buyurtma]
        print(f"{buyurtma.title()} narxi: {narx}")
    else:
        print(f"{buyurtma.title()} mavjud emas")



# =============================================================================
# while True:
#     mahsulot = input("Nima mahsulot kiritmoqchisiz?\n>>>")
#     narx = input(f"{mahsulot.title()}ning narxini tanlang:")
#     e_bozor[mahsulot] = int(narx)
#     sorov = input("Yana mahsulot kiritmoqchimisiz?(Ha\Yo'q)")
#     if sorov == "Yo'q":
#         break
# =============================================================================
    



