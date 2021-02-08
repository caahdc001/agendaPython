nome = "Cristiane"
idade = 33

minhaLista = ["azul", "amarelo", "rosa", "branco", "vermelho", "preto", "lilás"]

minhaLista.append("roxo") #adiciona elemento à lista

minhaLista.remove("azul") #remove elemento da lista, que neste caso é o azul

for cor in minhaLista:
    print(cor)

print("\n********************")

print(minhaLista[1]) #imprime um elemento específico da lista(começando pelo índice 0, após o azul ser removido, o rosa é o elemento de nº 1 na lista)

print("\n********************")

print(minhaLista[1:3]) #imprimindo com controle, escolhendo quais itens imprimir

print("\n********************")

print(nome[0:4])

print("\n********************")

for letra in nome:
    print(letra)