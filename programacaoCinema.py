cinema = {"The Grinch":"11:00hs", "Lagoa Azul":"15:00hs", "Batman":"17:00hs", "Crepúsculo":"18:00hs"}

print("\nConfira nossa programação de terça-feira\n")
for key in cinema:
    print (key)

filme = input("\nQue filme gostaria de assistir?\n")

horaSessao = cinema.get(filme)
if horaSessao == None:
    print("\n **Filme inválido, cheque novamente nossa programação abaixo e tente novamente.** \n")
    print("Programação:\n")
    for key in cinema:
        print (key)
else:
    print(f"\nO filme {filme} estará disponível na sessão das {horaSessao}")