#vytvoření pole a poté vypsaní do console
arrayA=[4, 8, 9, 7, 3]
print("pole:", arrayA)


#Pomocí metody append() bylo přídano slovo vítr
arrayA.append("vítr")
print("pole:", arrayA)


#Druhy prvek z pole byl odstraněn pomocí remove()
arrayA.remove(arrayA[1])
print("pole:", arrayA)


#5 indexová hodnota byla zaměněná za slunce
arrayA[4]="slunce"
print("pole:", arrayA)


#Byly přídany dvě stringové hodnoty pomocí extend()
arrayA.extend(["děšť, sníh"])
print("pole:", arrayA)
