# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:16:36 2022

@author: Dilshod
"""

#davlatlar = ["AQSH","O'zbekiston","Turkiya","Rossiya","Fransiya","Germaniya"]
#print(sorted(davlatlar))
#print(len(davlatlar))
#print(sorted(davlatlar,reverse=True))

#davlatlat1 = davlatlar.reverse()
#print(davlatlat1)
#davlatlar.sort()
#print(davlatlar)

#davlatlar.sort(reverse=True)
#print(davlatlar)

#j_sonlar = list(range(120,1200,2))

#summa = sum(j_sonlar)
#max1 = max(j_sonlar)
#min1 = min(j_sonlar)
#uzunlik = len(j_sonlar)
#print("Eng katta va eng kichik sonlar farqi:",max1-min1)

#print("Sonlar yig'indisi:",summa)

#print("Ro'yhad elementlari soni:",uzunlik)
#print(uzunlik)
#print("Ro'yhad boshidan 20 ta son\n>>>",j_sonlar[0:20])
#print("Ro'yhad o'rtasidan 20 ta son\n>>>",j_sonlar[530:550])
#print("Ro'yhad boshidan 20 ta son\n>>>",j_sonlar[-20:])

taomlar = ["Osh","Somsa","Kabob","Dimlama","Manti","Shashlik"]

nonushta = taomlar[:]

nonushta.remove("Manti")
nonushta.remove("Shashlik")
nonushta.append("Sutli osh")

print(nonushta)
print(taomlar)

nonushta = tuple(nonushta)
nonushta[0] = "Qaymoq va Non"




