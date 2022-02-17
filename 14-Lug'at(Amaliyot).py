# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:35:05 2022

@author: Dilshod
"""

#otam = {'ism':'azamat','yosh':43,'t_joy':'samarqand'}
#print(f"Otamni ismi {otam['ism'].title()}.U {otam['yosh']} yoshda.U {otam['t_joy']} viloyatida tug'ilgan.")

#oila_taom = {'ona':'osh','ota':'kabob','singil':'manti','uka':'somsa'}
#print(f"Onam { oila_taom['ona'] } ni yaxshi ko'radi")
#print(f"Otam { oila_taom['ota'] } ni yaxshi ko'radi")
#print(f"Ukam { oila_taom['uka'] } ni yaxshi ko'radi")
#print(f"Singlim { oila_taom['singil'] } ni yaxshi ko'radi")

phyton_lugat = {'integer':'butun son',
                'float':'haqiqiy son',
               'else':'yoki',
                'for':'uchun',
                'dictionary':'lug\'at',
                'string':'matn',
                'list':'ro\'yhad',
                'append':'qoshish',
                'remove':'o\'chirish',
                'name':'ism'
               }
soz = input("Biror so'z kiriting:").lower()
tarjima = phyton_lugat.get(soz)
if tarjima != None:
        print(">> ",phyton_lugat[soz]," <<")
else:
        print(">> Bunday so'z mavjud emas <<")
     

