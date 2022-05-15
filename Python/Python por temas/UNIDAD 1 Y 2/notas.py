# Realice un ejercicio que convierta notas de 1 a 5, con un decimal a letras
# segun la siguiente tabla:
# 1-2.9 => D
# 3 - 3.5 => R 
# 3.6 - 4 => B
# 4.1 - 5 => E

nota = float(input(f"Digite la nota numérica que desea convertir\n"))
if nota >= 1 and nota < 3:
    letra = "D"
elif nota >=3 and nota < 3.6:
    letra = "R"
elif nota >= 3.6 and nota <=4:
    letra = "B"
elif nota > 4 and nota <=5:
    letra = "E"
else:
    print("Digite una nota válida")
    letra = "inválida"

print(f"La nota es {letra}")
