""" first_value= 5 
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotiente: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent)) """

""" print(3 + 4 * 5)
print((3 + 4) * 5) """

""" first_value = 5
second_value = 4

quotient = first_value / second_value

print(type(quotient))
print(quotient) """

#Normalmente, você poderá trabalhar com valores int e float sem nenhum problema. Ocasionalmente, você precisará converter um float em um int.
#Às vezes, isso ocorre implicitamente (sem a sua instrução). Portanto, o ideal é você assumir ocontrole desse processo. 

""" pi = 3.14
print(type(pi))
print(int(pi))
print(round(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime))
print(round(uptime)) """

#A função round() fornece uma forma de fazer o arredondamento e a conversão de um valor float em um valor int.

first_value = round(7.654321, 2)
print(first_value)

second_value = round(9.87654, 3)
print(second_value)

#Ao fornecer um segundo argumento quando você chama a função round(), você pode controlar o número de casa decimais para o arredondamento.