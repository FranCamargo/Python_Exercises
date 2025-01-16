print("Conversor de Moeda")

dolar = 6.09

valorReal = float(input("Digite o valor em reais que você possui: "))

def calcularResultado(valorReal):
    return valorReal / dolar

resultado = calcularResultado(valorReal)

print(f"Você tem {resultado:.2f} em dólares")
