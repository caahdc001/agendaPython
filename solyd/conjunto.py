conjuntoCores = {"vermelho", "azul", "verde"} #assim como o dicionário, ele não é ordenado, ou seja, n~]ao dá pra buscar por item

conjuntoCores.add("branco")
conjuntoCores.add("vermelho") #ele não adiciona itens repetidos

print(conjuntoCores)

print("----------------------------------------------------------\n")

for cor in conjuntoCores:
    print(cor)

print("----------------------------------------------------------\n")

conjuntoCores.remove("azul")

print(conjuntoCores)