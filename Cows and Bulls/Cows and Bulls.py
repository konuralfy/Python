# Nasıl Oynanır ?
# 4 haneli sayı tahmin edilir
# Eğer girilen rakamlar doğruysa ve doğru yerindeyse Cow,
# Eğer girilen rakamlar doğruysa fakat yanlış yerdese Bull gösterilir.

#How To Play
#Guessing 4 digit number
#If picked numbers are correct and in the correct place you get Cow,
#If numbers are correct but in the wrong place you get Bulls.


import random

rand = random.randint(1000,9999)                                                  #Picks random 4 digit number

def inside(tahmin1,rand2,cow=0,bull=0):
    for i in range(4):
        if str(tahmin1)[i] == str(rand)[i]:                                       #Checks if number in correct place
            cow +=1
            continue
        elif str(tahmin)[i]in str(rand) and not str(tahmin1)[i] == str(rand)[i]:  #Checks if number is true but in wrong place
            bull +=1
            continue
        else:
            continue
    return(cow,bull)



while True:
    tahmin = int(input("Guess 4 digit number: "))

    if not len(str(tahmin)) == 4:
        print("Please enter 4 numbers\n")
        continue
    sonuc = inside(tahmin,rand)
    if sonuc[0] == 4:
        print ("Correct !")
    else:
        print ("Cows: ",sonuc[0],"Bulls: ",sonuc[1]," -- Try Again\n")
        continue
