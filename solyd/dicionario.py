dicionario = {
    "Chave": "Este é o valor da PRIMEIRA chave", #Criando outros objetos dentro de um dicionário, separados por vírgula
    "segundaChave": "Este é o valor da segunda chave"
}

#Um dicionário não possui índice. Ele é caracterizado pela chave e valor

print(dicionario) #imprime todo o dicionário

print("________________________________________________\n")

print(dicionario["Chave"]) #do dicionário, ele pega a chave(Chave), e mostra o valor...

print("________________________________________________\n")


for item in dicionario: #imprime cada item dentro do dicionário
    print(item)

print("________________________________________________\n")

for item in dicionario.values(): #pega cada item dentro do dicionário e imprime os valores
    print(item)

print("________________________________________________\n")
