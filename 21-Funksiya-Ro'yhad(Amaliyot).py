# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:07:00 2022

@author: Dilshod
"""

# =============================================================================
# def bosh_harf(royhad):
#     katta_harf = []   
#     while royhad:
#         soz = royhad.pop()
#         katta_harf.append(soz.title())
#     return katta_harf
# 
# royhad = ['islom','ahmad','dilshod','anvar'] 
# bosh_harfli = royhad[:]
# bosh_harfli_soz = bosh_harf(bosh_harfli)
# print(bosh_harfli_soz)      
# =============================================================================
   

def bahola(ismlar):
    baholi_talabalar = {}
    for ism in ismlar:
        talaba_bahosi = int(input(f"Talaba {ism.title()}ning bahosi:"))
        baholi_talabalar[ism.title()] = talaba_bahosi
    return baholi_talabalar

talabalar = ['aziz','dilshod','yashnarbek','javohir','maqsud','sardor']
baholanganlar = bahola(talabalar)
print(baholanganlar)
        
        