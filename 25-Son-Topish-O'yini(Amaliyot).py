# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 07:06:24 2022

@author: Dilshod
"""

import random as r

def son_top(x=10):
    sanagich = 0
    son = r.randint(1, x)
    print(f"Men 1 dan {x} gacha sonlardan bitta son o'yladim!")
    while True:
        sanagich = sanagich + 1
        taxmin = int(input("U qaysi son?:"))
        if taxmin>son :
            print("Taxmin soningiz meni sonimdan katta!") 
        elif taxmin<son:
            print("Taxmin soningiz meni sonimdan kichik!")
        else :
            print(f"Qoyil! Siz men o'ylagan sonni {sanagich} marta urinib topdingiz!\n\n\n")
            break
    return sanagich
        
def son_topaman(x=10): 
    sanagich = 0
    quyi = 1
    yuqori = x
    print(f"Siz 1 dan {x} gacha sonlardan bitta son o'ylang! Men topaman.") 
    tanlov = input("Birorta son o'ylang:(O'ylagan bo'lsangiz ENTER ni bosing?)")
    while True:
        sanagich = sanagich + 1
        if quyi != yuqori:
            taxmin = r.randint(quyi, yuqori)
        else :
            taxmin = quyi
        sorov = input(f"Siz {taxmin} sonini o'yladingiz?\n"
        f"(Bu son o'ylagan sondan katta bo'lsa(-),kichik bo'lsa(+),teng bo'lsa(T) bosing):")
        if sorov == '+':
            quyi = taxmin + 1
        elif sorov == '-':
            yuqori = taxmin - 1
        else :
            print(f"Qoyil! Siz o'ylagan sonni {sanagich} marta urinishda topdim!\n\n")
            break
    return sanagich
        

def oyin(x=10):
    """ 
    Bu funksiya ichida 2 ta o'yin bor,siz va cpu son topish o'yinlari,
    ichidagi x parametr bu o'ylagan sonlaringiz diapazoni hisoblanadi!
    
    """
    sorov = True
    while sorov:    
       men = son_top(x)    
       cpu = son_topaman(x)         
       if men>cpu:
           print(f"Men yutdim!!!({men}>{cpu})")
       elif men<cpu:
           print(f"Men yutqazdim!!!({men}<{cpu})")
       else :
           print(f"Durrang!!!({men}={cpu})")
       sorov = int(input("O'ynaymizmi?(Ha(1)/Yo'q(0):>>>"))
       
oyin(100)
       
       

    
                
        
        
    
    