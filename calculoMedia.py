print("Cálculo de médias")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

def soma(nota1, nota2, nota3):
    return nota1 + nota2 + nota3

total = soma(nota1, nota2, nota3)
media = total / 3

print(f"A média das notas é: {media: .2f}")
