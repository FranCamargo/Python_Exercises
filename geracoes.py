print("Descubra sua geração! ")

anoNasc = int (input("Digite o ano em que nasceu: "))

if anoNasc in range (1946,1964):
    print("Você é da geração boomer!")

elif anoNasc in range(1965,1980):
    print("Você é da geração X!")

elif anoNasc in range(1981,1996):
    print("Você é da geração Millenial - a melhor geração!")

else:
    print("Você é da geração Alpha ou é então muito velho kkk")