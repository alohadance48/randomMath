import math as math
import random as random
b = 1
while b :
    rand = random.randint(1, 360)
    if rand > 1 :
        print("Рандом: ", rand)
        sinus = math.sin(rand)
        cosinus = math.cos(rand)
        logariphm = math.log10(rand)
        print("Ваша рандомные cos sin logariphm:")
        print("Синус: ", sinus, "косинус: ", cosinus, "log10: ", logariphm) 

    if rand == 2 :
        break
    print ("Конец")