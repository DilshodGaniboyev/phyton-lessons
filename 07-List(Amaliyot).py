# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:27:54 2022

@author: Dilshod
"""

#ismlar = ["Dilshod",'Anvar',"Saddam"]
#print("Salom" ,ismlar[0] , "qalaysan?")
#print("Salom" , ismlar[1] , ".Nima qilyabsan?")
#print("Salom" , ismlar[2] , ".Choyhonaga borasanmi?")


#sonlar = [5,12,-45,5.46,8823]
#print(sonlar[0] + sonlar[1])
#print(sonlar[-1]-sonlar[1])
#sonlar[3] = 8
#sonlar.append(222)
#sonlar.insert(2, 45)
#print(sonlar)

#t_shaxslar = ['Amir Temur',"Al-Buxoriy","Abu Ali Ibn Sino"]
#z_shaxslar = ["Abror Muxtor Aliy","Shukurulloh","Abdulloh","Sardor"]

#t_shaxs = t_shaxslar.pop(1)
#z_shaxs = z_shaxslar.pop(0)

#print("Men tarixiy shaxslardan",t_shaxs,"bilan va zamonaviy shaxslardan",z_shaxs,"bilan suhbat qilishni juda istardim.")

friends = []
friends.append("Saddam")
friends.append("Azizbek")
friends.append("Anvar")
friends.append("Uchqun")
friends.append("Javohir")
friends.append("Maqsud")

print(friends)

friends.remove("Uchqun")
friends.remove("Maqsud")

print(friends)

friends.insert(0, "Yashnarbek")
friends.insert(2, "Jo'rabek")
friends.append("Shahriyor")

print(friends)
