print("Bem-vindo a Pedra Papel Tesoura Lagarto Spock")

import random

pedra = 1
papel = 2
tesoura = 3
lagarto = 4
spock = 5

print("Vamos começar!\n")


user_escolha = int(input("Escolha entre Pedra (1), Papel (2), Tesoura (3), Lagarto (4), Spock (5): "))
computer_escolha = random.randint(1, 5)

#Cria um dicionário de escolhas com chaves e valores representados por "key: value"
escolhas = {1: "Pedra", 2: "Papel", 3: "Tesoura", 4: "Lagarto", 5: "Spock"}

print(f"Você escolheu: {escolhas[user_escolha]}")
print(f"O computador escolheu: {escolhas[computer_escolha]}")


if user_escolha == computer_escolha:
    print("Empate!")
elif (user_escolha == 1 and (computer_escolha == 3 or computer_escolha == 4)) or \
     (user_escolha == 2 and (computer_escolha == 1 or computer_escolha == 5)) or \
     (user_escolha == 3 and (computer_escolha == 2 or computer_escolha == 4)) or \
     (user_escolha == 4 and (computer_escolha == 2 or computer_escolha == 5)) or \
     (user_escolha == 5 and (computer_escolha == 1 or computer_escolha == 3)):
    print("Você ganhou! :D")
else:
    print("Você perdeu :( Computer WINS :D")




