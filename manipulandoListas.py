# Lista de países
paises = ["Brasil", "Dinamarca", "EUA", "Japão", "India"]

print("Aqui estão os resultados da manipulação da lista.")

# Função append - adiciona item no final da lista
paises.append("Canadá")
print("Após append('Canadá'):", paises)

# Função extend - adiciona algo á lista e mostra após a mesma
paises.extend(["França", "Alemanha"])
print("Após extend(['França', 'Alemanha']):", paises)

# Função insert - insere na posição escolhida um valor na lista
paises.insert(2, "Austrália")
print("Após insert(2, 'Austrália'):", paises)

# Função remove - remove um item da lista
paises.remove("EUA")
print("Após remove('EUA'):", paises)

# Função pop - remove algo um item da lista.
popped_item = paises.pop()
print("Após pop():", paises, "| Item removido:", popped_item)

# Função clear - limpa a lista
paises.clear() 
print("Após clear():", paises)

# Redefinindo a lista de países para continuar com os exemplos
paises = ["Brasil", "Dinamarca", "EUA", "Japão", "India"]

# Função index - mostra a posição de um item da lista
index_japao = paises.index("Japão")
print("Índice de 'Japão':", index_japao)

# Função count - conta a quantidade de vezes que um item se repete na lista
count_brasil = paises.count("Brasil")
print("Contagem de 'Brasil':", count_brasil)

# Função sort - ordena os elementos da lista em ordem crescente (alfabética para strings e numérica para números). 
paises.sort()
print("Após sort():", paises)

# Função reverse - altera de trás pra frente os itens na lista
paises.reverse()
print("Após reverse():", paises)

# Função copy - faz uma copia da lista
copia_paises = paises.copy()
print("Cópia da lista:", copia_paises)
