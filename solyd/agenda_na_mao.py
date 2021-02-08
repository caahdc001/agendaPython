AGENDA = {
    "cris": {
        "tel": "933005529",
        "email": "chrismarinho25@gmail.com",
        "endereco": "av. boa vontade, 2062"
    },
    "maria": {
        "tel": "9999-1010",
        "email": "anamaria123@gmail.com",
        "endereco": "av. esperança, 450"
    },
    "ana": {
        "tel": "9999-1212",
        "email": "ana456@gmail.com",
        "endereco": "av. conquista, 2021"
    }
}

print("\n")

print(AGENDA) #mostra toda a agenda

print("-----------------------------------------------------\n")

print(AGENDA['maria']) #mostra um item específico dentro do dicionário(agenda)

print("-----------------------------------------------------\n")

print(AGENDA['maria']['endereco']) #filtrando item específico 

print("-----------------------------------------------------\n")

AGENDA['ana']['endereco'] = "Rua das Flores" #vá em agenda, entre no objeto ana, depois entre no endereço e altere o seu valor

print("-----------------------------------------------------\n")

print(AGENDA['ana']['endereco'])

print("-----------------------------------------------------\n")

#Adicionando mais um elemento no dicionário
AGENDA["lucas"] = {
    "tel": "9888-1212",
    "email": "lucas6@gmail.com",
    "endereco": "av. vitória, 98"
}

for contato in AGENDA:
    print(contato)

AGENDA.pop('ana')

print(AGENDA)