print("Quanto tempo você já viveu?\n")

idade = float(input("Quantos anos você tem? \n"))

def decadas(idade):
    return idade // 10  
# Usando // para obter o número inteiro de décadas

def anos(idade):
    return idade % 10  
# Usando % para obter o resto, que são os anos restantes

decadas_vividas = decadas(idade)
anos_vividos = anos(idade)

print(f"Você já viveu {decadas_vividas:.0f} décadas e {anos_vividos:.0f} ano/s.")
