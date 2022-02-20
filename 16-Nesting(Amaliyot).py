# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 06:15:34 2022

@author: Dilshod
"""

#shaxs0 = {'ism':'dilshod',
#          'yosh':20,
#          'til':'phyton',
#          'oyin':'puzzle'
#          }
#shaxs1 = {'ism':'Anvar',
#          'yosh':20,
#          'til':'c++',
#          'oyin':'fifteen'
#          }
#shaxs2 = {'ism':'Asilbek',
#          'yosh':16,
#          'til':'c#',
#          'oyin':'srp'
#          }
#shaxs3 = {'ism':'Azizbek',
#          'yosh':21,
#          'til':'java',
#          'oyin':'x-0'
#          }
#shaxslar = [shaxs0,shaxs1,shaxs2,shaxs3]
#for shaxs in shaxslar:
#    print(f"{shaxs['ism'].title()} "
#          f"{shaxs['til'].upper()} dasturlash tilida {shaxs['oyin'].upper()} o'yinini yaratgan.."
#          )


#kinolar0 = []
#kinolar1 = []
#kinolar2 = []

#shaxs_kino = {'onam':kinolar0,'otam':kinolar1,'ukam':kinolar2}

#for n in range(3):
#    kinolar0.append(input(f"Kinoni kiriting:"))
    
#for n in range(3):
#    kinolar1.append(input(f"Kinoni kiriting:"))
    
#for n in range(3):
#    kinolar2.append(input(f"Kinoni kiriting:"))

#for ism,kinolar in shaxs_kino.items():
#    print(f"{ism.title()} yoqtirgan filmlar:")
#    for kino in kinolar:
#        print(kino.title())

davlatlar = {'uzbekistan':{'m_yil':1991,'aholi':36_000_000,'p_birligi':'som'},
             'usa':{'m_yil':1776,'aholi':331_000_000,'p_birligi':'dollar'},
             'france':{'m_yil':1534,'aholi':67_500_000,'p_birligi':'yevro'}
             }

davlat = input("Biror davlat kiriting:").lower()

if davlat in davlatlar.keys():
    info = davlatlar[davlat]
    if davlat=='usa':
        davlat = davlat.upper()
    else :
        davlat = davlat.title()
    print(f"{davlat}ning ma'lumotlari:\n"
          f">>>Mustaqillik yili: {info['m_yil']}\n"
          f">>>Aholisi soni: {info['aholi']}\n"
          f">>>Pul birligi: {info['p_birligi'].upper()}\n"
          )
else :
    print("Bu davlat haqida ma'lumot topilmadi!!!")





#for davlat,malumot in davlatlar.items():
#    if davlat=='usa':
#      davlat=davlat.upper()
#    else :
#        davlat=davlat.capitalize()
#    print(f"{davlat} davlatining malumotlar:")
#    print(f"Mustaqillik yili: {malumot['m_yil']}\n"
#          f"Aholi soni: {malumot['aholi']}\n"
#          f"Pul birligi: {malumot['p_birligi'].upper()}\n"
#          )
        
        
        
    
    
        




