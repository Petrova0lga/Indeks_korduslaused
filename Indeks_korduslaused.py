
from math import *
j=0
for i in range(0,15,1): #for i in range(15)
    A=float(input(f"{i+1} Sisesta A : "))
    if int(A)==A:
        j+=1
print(j)

j=0
i=0
while True:
    i+=1
    A=float(input(f"{i} Sisesta A : "))
    if int(A)==A:
        j+=1
    if i==15: break
print(j)

j=0
i=0
while i<15:
    i+=1
    A=float(input(f"{i} Sisesta A : "))
    if int(A)==A:
        j+=1
print(j)


print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(nimi, "Oi, kui ilus nimi!")
a=input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if a=="1":

    while True:
        try:
            pikkus=int(input("Pikkus: "))#  text
            if pikkus>0 and pikkus<273: break
        except:
            print("Error")
    mass=-1
    while mass<0 or mass>400: #mass=int(input("Mass: "))
        try:
            mass=int(input("Mass: "))
        except:
            print("Error")
           
        try:
            index=mass/pikkus
        except:
            mass=55
            print("Error, siis mass= 55")
    index=round(mass/(0.01*pikkus*pikkus),2)
    print(nimi, "! Sinu keha index on: ", index)
    if index<16:
        print("Tervisele ohtlik alakaal")
    elif index>=16 and index<19:
        print("Alakaal")
    elif index>=19 and index<25:
        print("Normaalkaal")
    elif index>=25 and index<30:
        print("Ülekaal")
    elif index>=30 and index<35:
        print("Rasvumine")
    elif index>=35 and index<40:
        print("Tugev rasvumine")
    elif index>40:
        print("Tervisele ohtlik rasvumine")
else:
    print("Kahju! See on väga kasulik info!")
print("")
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")