colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown'] #lista (separada por colchetes)

#Um identificador é a referência a todos os itens da lista. Nesse caso, o identificador é a variável colors.

#print(colors)
#print(type(colors))

#print(f'0-based indexing into the list ... second item: {colors[1]}')

#print(f'Last item of the list: {colors[-1]}') #Podemos usar números negativos como índices para contagem retroativa do final da lista.

#print(f'Next to last item in the list: {colors[-2]}') #...Então, quando usamos o índice [-1], acessamos o último item. Quando usamos o índice [-2], acessamo o penúltimo item e assim por diante.

""" print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a SLICE, starting at index 0 to index 3:')
print(colors[:3])

print('\nPrint a slice, atarting a index 4 to the end of the list:')
print(colors[4:])

print('\nPrint a slice, from the 4th from the end (but not the last item):')
print(colors[-4:-1]) """

colors.reverse()
print(colors)

colors.sort()
print(colors)