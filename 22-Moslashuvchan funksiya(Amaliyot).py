# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:34:03 2022

@author: Dilshod
"""

# =============================================================================
# def kopaytir(x,y,*sonlar):
#     kopaytirma = 1
#     for n in sonlar:
#         kopaytirma = kopaytirma * n
#     return kopaytirma
# 
# print(kopaytir(1,2,3,4))
# print(kopaytir(-2,1,-8,-3))
# print(kopaytir(0,1,1,2,3,4,3,5,6))
# =============================================================================


def talaba_malumot_ber(ism,familia,**malumotlar):
    """ Talaba haqidagi ma'lumotlar beriladigan funksiya """
    malumotlar['ism'] = ism
    malumotlar['familia'] = familia
    return malumotlar

talaba1 = talaba_malumot_ber('dilshod', 'ganiboyev', tugilgan_yil=2002,tugilgan_shaxar = 'samarqand')
talaba2 = talaba_malumot_ber('yashnarbek', 'samiyev', tugilgan_yil=2002,tugilgan_shaxar = 'qarshi')
talaba3 = talaba_malumot_ber('maqsud', 'mardiev', tugilgan_yil=2000,tugilgan_shaxar = 'samarqand')

talabalar = [talaba1,talaba2,talaba3]
for talaba in talabalar:
    print(talaba)
