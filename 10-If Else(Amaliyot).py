# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 06:24:33 2022

@author: Dilshod
"""

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

#for car in cars:
#    if car != "gm":
#      print(car.title())
#    else: print(car.upper())

#ism = input("Iltimos ismingizni kiriting:")
#if ism == "admin":
#    print("Xush kelibsiz, Admin.Foydalanuvchilar oynasini ko'rasizmi?")
#else : print(f"Xush kelibsiz, {ism}.")

#son1 = int(input("Birinchi son:"))
 
#son2 = int(input("Ikkinchi son:"))

#if son1 == son2 :print("Ikkala son teng")

son = int(input("Istalgan son yozing:"))
#print("Musbat son") if son>=0 else print("Manfiy son")

if son>=0: 
    print(son**(0.5))
    
else : 
    print("Iltimos musbat son kiriting!")
