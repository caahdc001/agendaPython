""" message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize()) """

# A função *capitalize()* garante que o primeiro caractere em uma cadeia de caracteres esteja em letra maiúscula. 
# Somente a primeira letra da cadeia de caracteres é maiúscula. 

message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())

location = 'Mississippi'
print(location.count('s'))

# O método count() fornece uma contagem do número de vezes que um caracter espicificado é usado em uma cadeia de caracteres.

""" print(len('how many letters in this string?')) """

# Método len() fornece a contagem da cadeia de caracteres especificada 

""" message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar')) """

# Chame as fuções startswith() e endswith() para inspecionar o conteúdo de uma cadeia de caracteres para descobrir se ela corresponde àquilo com que
# você esperava que ela começasse ou terminasse, respectivamente.

""" message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T')) """

# O método find() localiza a posição de base zero de uma cadeia de caracteres dentro de outra cadeia de caracteres.
# Em outras palavras, começando com o número 0, o método informa a localização da cadeia de caracteres de pesquisa.

""" message = '    middle    '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.') """

# O Python fornece a função lstrip() para remover caracteres de espaço vazios do lado esquerdo de uma cadeia de caracteres e a função
#rstrip() para removê-los do lado direito de uma cadeia de caracteres. Outra opção é usar a função strip() para remover ambos.

""" message  = 'brevity is the essence of wit'
message  = message.replace('essence', 'soul')
print(message) """

# A função replace() troca cada instância de uma cadeia de caracteres por uma cadeia de caracteres diferente.

""" message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-')) """

#Os métodos rjust() e ljust() adicionam caracteres de espaço vazio a uma cadeia de caracteres 
# para justificar à direita ou à esquerda, respectivamente.

