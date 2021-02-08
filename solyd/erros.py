# Erros em tempo de compilação
# Erros em tempo de execução -> mais comuns
# Erros de lógica -> comportamento inesperadi do programa


""" def divisao(a, b):
    try:
        print(a/b)
    except Exception as e:
        print('Divisão inválida')
        print(e)


divisao(20, 0) """


try:
    a = float(input('Digite o número A: ')) #ValueError possível
    b = float(input('Digite o número B: '))

    print(a/b) #ZeroDivisionError possível
except ValueError as error:
    print('Input inválido, digite apenas números')
except ZeroDivisionError as error:
    print('Não pode ser feita divisão por zero')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)
finally:
    print('Fim do programa')