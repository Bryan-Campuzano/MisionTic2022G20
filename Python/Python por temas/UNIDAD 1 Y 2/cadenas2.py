animal = "cocodrilo" #cocodrilo tiene 9 letras
print(len(animal))
print(animal[4])
print(animal[-2])
print(animal[2:6]) # el primer n+umero está incluido y el segundo no está incluido
print(animal[:4])
print(animal[4:])
print("zas" in animal)

print("-----------------")

for i in range(len(animal)): #0-8
    print(animal[i])
    
print("-----------------")
    
for i in animal: #i va tomando los valores de cada caracter
    print(i)
    
    
