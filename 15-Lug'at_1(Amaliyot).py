# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 23:33:41 2022

@author: Dilshod
"""

#phyton_lugat = {'integer':'butun son',
#                'float':'haqiqiy son',
#                'else':'yoki',
#                'for':'uchun',
#                'dictionary':'lug\'at',
#                'string':'matn',
#                'list':'ro\'yhad',
#                'append':'qoshish',
#                'remove':'o\'chirish',
#                'name':'ism'
#                }
#for key,value in sorted(phyton_lugat.items()):
#        print(f"Key: {key}")
#        print(f"Value: {value}\n")

#davlat_poytaxt = {'uzbekistan':'tashkent',
#                  'great britian':'london',
#                  'france':'paris',
#                  'itaia':'rome',
#                  'usa':'washington'
#                  }

#for davlat in sorted(davlat_poytaxt.keys()):
#    print(davlat.title())   
#for poytaxt in sorted(davlat_poytaxt.values()):
#    print(poytaxt.title())

#davlat = input("Davlat kiriting:")
#if davlat in davlat_poytaxt.keys():
#    print(f"Poytaxti:{davlat_poytaxt[davlat].title()}")
#else:
#    print("Bunday ma'lumot yo'q")
  
taom_narx = {'osh':20000,
             'kabob':15000,
             'somsa':8000,
             'shashlik':12000,
             'qozonkabob':22000,
             'norin':18000,
             'lagmon':18000,
             'lavash':21000,
             'hot-dog':19000,
             'choy':5000
             }  

taomlar = []
print("3 ta taom buyurtma qiling!\n>>>")
for taom in range(3):
    taomlar.append(input(f"{taom+1}-Taom:"))

for taom in taomlar:
    if taom in taom_narx.keys():
        print(f"{taom}ning narxi: {taom_narx[taom]}")
    else :
        print(f"Kechirasiz,bizda {taom} hozircha tayyor emas!")
    
    
    
    
    
    
    
    
    
    
    
    