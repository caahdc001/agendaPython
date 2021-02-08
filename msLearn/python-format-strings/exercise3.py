""" medicine = 'Coughssin'
dosage = 5 
duration = 4.5

instructions = '{} - Take {}  ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
print(instructions)
 """
#Neste exemplo de código, definimos uma cadeia de caracteres de formato que contém uma série de campos de substituição conforme 
#definido por um conjunto de chaves{}.

#A função format() é poderosa e flexível. Você pode obter a mesma funcionalidade com menos digitação usando literais de cadeia de caracteres
# formatados, também conhecidos como cadeis de caracteres f.

""" name = 'World'
message = f'Hello, {name}.'
print(message)

count = 10   # variável definida com um valor de int
value = 3.14   # variável definida como um valor de float
message = f'count to {count}.  Multiply by {value}.' # a cadeia de cararteres de formato cuida da conversão de tipo para nós, portanto, não precisamos chamar str() em relação a esses valores.
print(message) """

""" width = 5
height = 10

print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.') """

value = 'hi'

print(f'.{value:<25}.') #Alinha à esquerda deixando um espaço de 25 caracteres
print(f'.{value:>25}.') #Alinha à direita após um espaço de 25 caracteres
print(f'.{value:^25}.') #Centraliza entre um espaço de 25 caracteres
print(f'.{value:-^25}.') #Centraliza entre os traços - especificados no format

#Um especificador de formato usa um símbolo de dois-pontos (:) após o nome da variável para especificar como esse valor deve ser formatado.

# Sintaxe do especificador de formato para adicionar alinhamento e preenchimento às cadeias de caracteres de formato. 