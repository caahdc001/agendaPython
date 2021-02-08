tuplasCores = ("amarelo", "azul", "roxo") #pode-se usar parênteses ou deixar apenas as strings soltas
listaCores = ["amarelo", "azul", "roxo"]

listaCores.append("vermelho") #adicionando elemento na lista
listaCores[1] = "branco" #alterando elemento da lista

#A tupla é estática, não se pode adicionar, remover elementos ou alterar

print(tuplasCores)

print("\n*********************************")

print(listaCores)

print("\n*********************************")

for cor in tuplasCores:
    print(cor)