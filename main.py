import pandas as pd
import os
import shutil

# read by default 1st sheet of an excel file
data = pd.read_excel('Video-Classification-GT.xlsx')
print(data)


print("-------------------- For Copy all Logo Videos to new folder --------------------")

logo = data[data['Category'] == 'Logo']
print(logo)


logo1 = data[data['Category'] == 'Logo'] ['Filename']
print(logo1)

for item in logo1:
   print(item)

sourse='E:/User Sahil/Desktop/Miniproject/Videos/'
destination='E:/User Sahil/Desktop/Miniproject/Raw dataset/Logo/'

#files = os.listdir(sourse)

for item in logo1:
    shutil.copy(sourse+item, destination+item )
    print("Files are copied successfully")

print("-------------------- Logo Videos are copied successfully --------------------")
print(" ")
print(" ")
print(" ")
print(" ")


print("-------------------- For Copy all Animation Videos to new folder --------------------")

Animation = data[data['Category'] == 'Animation']
print(Animation)


Animation1 = data[data['Category'] == 'Animation'] ['Filename']
print(Animation1)

for item in Animation1:
   print(item)

sourse='E:/User Sahil/Desktop/Miniproject/Videos/'
destination='E:/User Sahil/Desktop/Miniproject/Raw dataset/Animation/'

#files = os.listdir(sourse)

for item in Animation1:
    shutil.copy(sourse+item, destination+item )
    print("Files are copied successfully")

print("-------------------- Animation Videos are copied successfully --------------------")

print(" ")
print(" ")
print(" ")
print(" ")


print("-------------------- For Copy all IndoorLab Videos to new folder --------------------")

IndoorLab = data[data['Category'] == 'IndoorLab']
print(IndoorLab)


IndoorLab1 = data[data['Category'] == 'IndoorLab'] ['Filename']
print(IndoorLab1)

for item in IndoorLab1:
   print(item)

sourse='E:/User Sahil/Desktop/Miniproject/Videos/'
destination='E:/User Sahil/Desktop/Miniproject/Raw dataset/IndoorLab/'

#files = os.listdir(sourse)

for item in IndoorLab1:
    shutil.copy(sourse+item, destination+item )
    print("Files are copied successfully")

print("-------------------- IndoorLab Videos are copied successfully --------------------")