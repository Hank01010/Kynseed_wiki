# -*- coding: utf-8 -*-
"""Kynseed.ipynb

# Files needed:
*   AllItems.txt
*   EAItems.txt
*   ItemRatingConditions.xml
*   ItemTraitDetails.xml
*   FishSpawn.xml
*   ApothRecipes.xml
*   ALlRecipes.txt
"""

from xml.dom import minidom

"""**Storing Item ID in list**"""

with open('EAItems.txt') as f:
    lines = [line.rsplit('|') for line in f]

ids = [int(line[0]) for line in lines]
names = [line[1] for line in lines]

with open('AllItems.txt') as f:
    lines = [line.rsplit('|') for line in f]

ids2 = [int(line[0]) for line in lines]
names2 = [line[1] for line in lines]

"""# Recipes"""

with open('AllRecipes.txt') as f:
    ing = f.read().splitlines()
    rec = [line.rsplit(',') for line in ing]
    res = [[int (l) for l in k] for k in rec]
print(res)
recipes =  []

for k in res:
  temp_list = [""]
  for l in k:
    for m in range(0, len(ids)):
      if l == ids[m]:
        if l == k[len(k)-1]:
         temp_list[0] = (names[m])
        else:
          temp_list.append(names[m])
    for m in range(0, len(ids2)):
      if l == ids2[m]:
        if l == k[len(k)-1]:
         temp_list[0] = (names2[m])
        else:
          temp_list.append(names2[m])
  recipes.append(temp_list)


print(recipes)

#Dictionary for skill

ToolSkill = {1:"Neophyte",2:"Novice",3:"Apprentice",4:"Journeyman",5:"Craftsman",6:"Artistan",7:"Adept",8:"Expert",9:"Master",10:"Legendary"}

"""**Rating conditions**"""

mydoc = minidom.parse('ItemRatingConditions.xml')
items = mydoc.getElementsByTagName('ItemRatingConditions')

I = items[0]

ID = I.getElementsByTagName('UID')[0].firstChild.data #get Id
ID = I.getElementsByTagName('UID')[0]
print(ID.childNodes)

print(ids[23])

from os import linesep
Star =[]
for item in items:
  print("***")
  li =[]  
  
  CH = item.childNodes

  UID = int(CH[1].childNodes[0].data)

  for k in range(0,len(ids)):
    if UID==ids[k]:
      print(names[k])
      li.append(names[k])
      break
  for k in range(0,len(ids2)):
    if UID==ids2[k]:
      print(names2[k])
      li.append(names2[k])
      break

  print("ID:" + str(UID))
  
  li.append("ID:" + str(UID))
  
  for i in range(3,min(10, len(CH)),2): 
    if CH[i].hasChildNodes():
      temp = CH[i].childNodes[1]
      print(str(CH[i].attributes[ 'xsi:type'].value)[10:len(str(CH[i].attributes[ 'xsi:type'].value))]+ ': ' +str(temp.childNodes[0].data))
      li.append(str(CH[i].attributes[ 'xsi:type'].value)[10:len(str(CH[i].attributes[ 'xsi:type'].value))]+ ': ' +str(temp.childNodes[0].data))
    else:
      print(str(CH[i].attributes[ 'xsi:type'].value)[10:len(str(CH[i].attributes[ 'xsi:type'].value))] + ': ' +str(CH[i].attributes[ 'type'].value))
      li.append(str(CH[i].attributes[ 'xsi:type'].value)[10:len(str(CH[i].attributes[ 'xsi:type'].value))] + ': ' +str(CH[i].attributes[ 'type'].value))
  Star.append(li)
  
print(Star)

print

"""**Item traits**"""

mydoc = minidom.parse('ItemTraitDetails.xml')
items = mydoc.getElementsByTagName('ItemTraitDetails')

Trait = []
for item in items: 
  li = []
  CH = item.childNodes

  UID = int(CH[1].childNodes[0].data)
  #print(CH)
  print("***")
  for k in range(0,len(ids)):
    if UID==ids[k]:
      li.append(names[k])
      print(names[k])
      break
  for j in range(0,len(ids2)):
    if UID==ids2[j]:
      li.append(names2[j])
      print(names2[j])
      break
  li.append("ID:" + str(UID))
  print("ID:" + str(UID))
  li.append('Tier: '+str(CH[3].childNodes[0].data))
  print('Tier: '+str(CH[3].childNodes[0].data))
  print('Traits:')
  for  i in range(3,min(10, len(CH)), 2) : # for i in range(5,I.childNodes.length, 2) : i in range(3,min(10, len(CH)),2)
    temp = CH[i].childNodes
    for k in range(1,len(temp),2):
      li.append(' ' + str(temp[k].childNodes[0].data))
      print(' -' + str(temp[k].childNodes[0].data))
  Trait.append(li)

print(Trait)

"""**Symptoms**

""
with open('Symptoms.txt') as f:
    l= [line.rsplit('|=')[0:2] for line in f]

tmp=0

for i in l:
  if "Symptom0NPCComment" in i[0] or "Symptom1NPCComment" in i[0]:
    if  i[0][18:len(i[0])] == tmp:
      print("               "+ str(i[1]))
    else:
      print(i[0][18:len(i[0])] + ": "+ i[1])
    
    tmp = i[0][18:len(i[0])]
"""

mydoc = minidom.parse('Ailments.xml')
items = mydoc.getElementsByTagName('Symptom')

Symptom = []
Apoth = []
for item in items: 
  li = []
  CH = item.childNodes
  li.append(str(CH[3].childNodes[0].data))
  print('Tag: '+str(CH[3].childNodes[0].data))
  for  i in range(3,min(10, len(CH)), 2) : # for i in range(5,I.childNodes.length, 2) : i in range(3,min(10, len(CH)),2)
    temp = CH[i].childNodes
    for k in range(1,len(temp),2):
      li.append(' ' + str(temp[k].childNodes[0].data))
      print(' -' + str(temp[k].childNodes[0].data))
  
  li.append(str(CH[7].childNodes[0].data))

  Symptom.append(li)

print(Symptom)

items = mydoc.getElementsByTagName('Malady')

Malady = []
Apoth = []
for item in items: 
  li = []
  CH = item.childNodes
  li.append(str(CH[3].childNodes[0].data))
  print('Tag: '+str(CH[3].childNodes[0].data))
  print('Cure Traits:')
  for  i in range(3,min(10, len(CH)), 2) : # for i in range(5,I.childNodes.length, 2) : i in range(3,min(10, len(CH)),2)
    temp = CH[i].childNodes
    for k in range(1,len(temp),2):
      li.append(' ' + str(temp[k].childNodes[0].data))
      print(' -' + str(temp[k].childNodes[0].data))
  
  li.append(str(CH[7].childNodes[0].data))

  Malady.append(li)

print(Malady)

"""**fish spawn**"""

mydoc = minidom.parse('FishSpawn.xml')
items = mydoc.getElementsByTagName('FishSpawn')

Fish = []
for item in items:
  li =[]
  print("***")  

  CH = item.childNodes[1].childNodes

  UID = int(item.attributes['UID'].value)
  Region = item.attributes['region'].value
  WaterType = item.attributes['circumstance'].value
  
  for k in range(0,len(ids)):
    if UID==ids[k]:
      li.append(names[k])
      print(names[k])
      break
  for k in range(0,len(ids2)):
    if UID==ids2[k]:
      li.append(names2[k])
      print(names2[k])
      break

  print("ID:" + str(UID))
  if Region != "NONE":
    print("Found in: " + Region)
    li.append("Found in: " + Region)
  print("Caught in: " + WaterType)
  li.append("Caught in: " + WaterType)
  li.append("SpawnConditions:")
  for i in range(1,min(10, len(CH)),2): 
      temp = CH[i]
      li.append(str(temp.childNodes[0].data))
      print(str(temp.tagName) + ': ' +str(temp.childNodes[0].data))
  Fish.append(li)
print(Fish)

f = open("KW_Recipes.txt", "w+")
for i in recipes:
  for k in i:
    if k == i[len(i)-1]:
      l =  str (k)
    else:
      l = str(k) + ", "
    f.write(l)
  f.write("\n")

f = open("KW_StarRating.txt", "w+")
for i in Star:
  for k in i:
    if k == i[len(i)-1]:
      l =  str (k)
    else:
      l = str(k) + ", "
    f.write(l)
  f.write("\n")

f = open("KW_ItemTraits.txt", "w+")
for i in Trait:
  for k in i:
    if k == i[len(i)-1]:
      l =  str (k)
    else:
      l = str(k) + ", "
    f.write(l)
  f.write("\n")

f = open("KW_FishSpawn.txt", "w+")
for i in Fish:
  for k in i:
    if k == i[len(i)-1]:
      l =  str (k)
    else:
      l = str(k) + ", "
    f.write(l)
  f.write("\n")

f = open("KW_ApothCures.txt", "w+")
for i in Symptom:
  for k in i:
    if k == i[len(i)-1]:
      l =  str (k)
    else:
      l = str(k) + ", "
    f.write(l)
  f.write("\n")

for i in Malady:
  for k in i:
    if k == i[len(i)-1]:
      l =  str (k)
    else:
      l = str(k) + ", "
    f.write(l)
  f.write("\n")

f = open("KW_ToolQualityDict.txt","w+" )
f.write('1:"Neophyte",2:"Novice",3:"Apprentice",4:"Journeyman",5:"Craftsman",6:"Artistan",7:"Adept",8:"Expert",9:"Master",10:"Legendary"')
