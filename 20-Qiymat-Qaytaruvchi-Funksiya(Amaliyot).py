# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:25:25 2022

@author: Dilshod
"""

# =============================================================================
# def shaxs_info(ism,familia,t_yil,t_joy,e_mail='',tel_raqam=''):
#     
#     """ Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
#     email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya """
#     
#     shaxs = {'ism':ism,
#             'familia':familia,
#             'tugilgan_yil':t_yil,
#             'tugilgan_joy':t_joy,
#             'e_mail':e_mail,
#             'telefon_raqam':tel_raqam
#             }
#     return shaxs
# 
# shaxs1 = shaxs_info('dilshod','ganiboyev','2002','samarqand','ganiboyevdilshod2002@gmail.com')
# shaxs2 = shaxs_info('anvar','ishmamatov','2002','samarqand','forexample@gmail.com','+998332440333')
# shaxs3 = shaxs_info('azizbek','ziyodov','2002','samarqand')
# 
# mijozlar = [shaxs1,shaxs2,shaxs3]
# x=True
#  
# if mijozlar:  
#         for shaxs in mijozlar:
#             print(
#                 f"Ismi:{shaxs['ism'].title()}\n"
#                 f"Familiasi:{shaxs['familia'].title()}\n"
#                 f"Tug'ilgan yili:{shaxs['tugilgan_yil']}\n"
#                 f"Yoshi:{2022-int(shaxs['tugilgan_yil'])}\n"
#                 f"Tug'ilgan joyi:{shaxs['tugilgan_joy'].upper()}\n"
#                 f"E-Mail:{shaxs['e_mail']}\n"
#                 f"Tel raqami:{shaxs['telefon_raqam'].upper()}\n\n"
#                 ) 
# =============================================================================

# =============================================================================
# def eng_katta(x,y,z):
#     max = 0
#     if x>y and x>z:
#         max = x
#     elif z>x and z>y:
#         max = z
#     else :
#         max = y
#         
#     return max
#         
# son1 = int(input("Birinchi son:"))
# son2 = int(input("Ikkinchi son:"))
# son3 = int(input("Uchinchi son:"))
# 
# print(eng_katta(son1,son2,son3))
# =============================================================================
          
# =============================================================================
# PI = 3.14
# def aylana_info(radius):
#     aylana = {'radiusi':radius,
#               'diametri':2*radius,
#               'perimetri':2*PI*radius,
#               'yuzi':PI*(radius**2)
#               }     
#     return aylana 
# 
# radius = int(input("Aylana radiusini kiriting:"))
# 
# aylana  = aylana_info(radius)
# 
# print(f"Radiusi: {aylana['radiusi']}\n"
#       f"Diametri: {aylana['diametri']}\n"
#       f"Perimetri: {aylana['perimetri']}\n"
#       f"Yuzasi: {aylana['yuzi']}\n\n"
#       )      
# =============================================================================

# =============================================================================
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
# 
#     return tub_sonlar    
# 
# input(tub_sonlar_top(1, 100))
#           
# =============================================================================

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar

son = int(input("Biror son kiriting:"))

print(fibonacci(son))

