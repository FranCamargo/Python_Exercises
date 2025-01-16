print("Identificando palíndromos")

# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas
palavra = palavra.replace(" ", "").lower()

""" Verifica se a palavra é igual à sua versão invertida
 em [::-1] quer dizer que deixamos em branco início e meio e -1 
 que começamos a ler a palavra de trás pra frente"""
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
