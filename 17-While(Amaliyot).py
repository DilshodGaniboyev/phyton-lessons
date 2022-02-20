# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:16:17 2022

@author: Dilshod
"""

# =============================================================================
# savol = "Yaxshi ko'rgan kitobingizni kiriting?\n"
# savol += "((To'xtatish uchun (STOP) deb yozing))\n>>>"
# chiqish = ''
# while chiqish=='':
#     javob = input(savol)
#     if javob == 'STOP':
#         chiqish = 'exit'
# print('Dastur tugadi!')
# =============================================================================


# =============================================================================
# while True:
#     yosh = input("Yoshingizni kiriting:\nChiqish uchun (quit)\n>>>")
#     if yosh!='quit':
#         if float(yosh)<7:
#             bilet=2000
#         elif float(yosh)>=7 and float(yosh)<18:
#             bilet=3000
#         elif float(yosh)>=18 and float(yosh)<65:
#             bilet=10000
#         else : 
#             bilet=0
#         print(bilet)
#     else :
#         break
# print("Dastur tugadi!")
# =============================================================================
      
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
        

    

    

    




