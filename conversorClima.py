print("Sistema: Como está o clima hoje? ")

temp = float(input("Informe a temperatura em Celsius: \n"))
querConverter = input("Você gostaria de converter a temperatura para Farenheit? \n Sim (S), Não (N)").upper()


if querConverter == "S":
    tempF = temp * 1.8 + 32
    print(f"A temperatura é equivalente a {tempF:.2f} graus em Farenheit")
else:
    print("Confira abaixo como está o clima em Celsius: ")

if temp >= 32:
        print(f"Hoje está calor!")
elif temp <32 and temp >= 17:
        print("O clima está ameno.")
else:
     print("O clima está frio.") 
