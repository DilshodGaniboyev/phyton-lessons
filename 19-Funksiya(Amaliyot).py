# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:12:23 2022

@author: Dilshod
"""


# =============================================================================
# son = int(input("Biror son kiriting:"))
# 
# def son_kub_kva(son):
#     """ Sonning kvadrati va kubini chop etadigan dastur!"""
#     print(f"{son}ning kubi {son**3} !\n"
#           f"{son}ning kvadrati {son**2} !"
#           )
#     
# son_kub_kva( son ) 
# =============================================================================
 

   
# =============================================================================
# son = int(input("Biror son kiriting:"))
# 
# def juft_toq(son):
#     """ Sonning juft yoki toqligini chop etadigan dastur!"""
#     if son%2==0:
#         print(f"{son} juft !\n")
#     else :
#         print(f"{son} toq !")
#           
#     
# juft_toq( son )
# =============================================================================

# =============================================================================
# son1 = int(input("Birinchi son kiriting:"))
# son2 = int(input("Ikkinchi son kiriting:"))
# 
# def katta_kichik(son1,son2):
#     """ Sonning katta yoki kichikligini chop etadigan dastur!"""
#     if son1>son2:
#         print(f"{son1} {son2}dan katta !\n")
#     elif son1<son2 :
#         print(f"{son2} {son1}dan katta !\n")
#     else:
#         print("Sonlar teng!")
#     
# katta_kichik(son1, son2) 
# =============================================================================

# =============================================================================
# x = int(input("x sonni kiriting:"))
# y = int(input("y sonni kiriting:"))
# 
# def x_daraja_y(son1,son2):
#     """ Sonning x y darajadagi qiymatini chop etadigan dastur!"""
#     print(f"{son1} ning {son2} darajasi: {x**y}")
#     
# x_daraja_y(x, y) 
# =============================================================================

# =============================================================================
# x = int(input("x sonni kiriting:"))
# y = int(input("y sonni kiriting:"))
# 
# def x_daraja_y(son1,son2=2):
#     """ Sonning x y darajadagi qiymatini chop etadigan dastur!"""
#     print(f"{son1} ning {son2} darajasi: {son1**son2}")
#     
# x_daraja_y(x) 
# =============================================================================

son = int(input("Biror son kiriting:"))

def qoldiqsiz_bol(son):
    for n in range(2,10):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi ")
# =============================================================================
#         else:
#             print(f"{son} {n} ga qoldiqli bo'linadi ")
# =============================================================================
            
qoldiqsiz_bol(son)
            