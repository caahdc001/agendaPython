""" print(type('7'))
print(type(7))
print(type(7.1)) """

# A função type() simplesmente examina o valor transmitido como um parâmetro de entrada (a palavra entre parênteses)
#e retorna o tipo de dados.

print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))

# A função isistance() retorna um valor booliano

# Os valores têm tipos de dados e as variáveis não. Uma variável é simplesmente apontada para um valor e pode apontar para qualquer tipo de dados. 