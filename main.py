import random

#Jednorozměrné pole - úvod 
pole=[89, 8, 69, 7, 4, 10 ,20 ,100, 1 ] 
print(pole)

#vypiše se první, prostřední a poslední hodnota
print(pole[0])
print(pole[4])
print(pole[8])

#5 indexova hodnota byla zaměňena za 34
pole[5]=34
print(pole)

#hodnota indexu 7 je vypsaná z pole
print(pole[7])

#délka pole
print(len(pole))

#min a max hodnota pole
print(min(pole))
print(max(pole))

#druhé pole 
pole2=[4, 5, 8, 74, 3, 0, 7, 56, 250]

#sečítaní pole  
print(sum(pole2))

#sečítaní indexove hodnoty 1 a 5 z pole2
print(pole2[1]+pole2[5])

#BONUS  
random.shuffle(pole2)
print(pole2)


