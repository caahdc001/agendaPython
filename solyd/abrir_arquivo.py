try:
    with open('D:\Chris\Programming\sweigart\solyd\emails.txt') as arquivo:
        print(arquivo.readlines())
except FileNotFoundError:
    print('Arquivo não existe')