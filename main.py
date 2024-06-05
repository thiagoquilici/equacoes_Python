import math

# função calcular equações
def calcular_equacao():
    opcao = input('Escolha o tipo de equação (1 para 1º grau, 2 para 2º grau): ')

    if opcao == '1':
        a = float(input("Digite o valor de 'a': "))
        b = float(input("Digite o valor de 'b': "))
        yield calcular_equacao_primeiro_grau(a, b)
    elif opcao == '2':
        a = float(input("Digite o valor de 'a': "))
        b = float(input("Digite o valor de 'b': "))
        c = float(input("Digite o valor de 'c': "))
        yield calcular_equacao_segundo_grau(a, b, c)
    else:
        yield print('Opção inválida. Escolha 1 ou 2.')

# função equação de 1º grau
def calcular_equacao_primeiro_grau(a, b):
    if a == 0:
        return print("O coeficiente 'a' não pode ser zero.")
    x = -b / a
    return print(f'A solução da equação de 1º grau é x = {x}.')

# função equação 2º grau
def calcular_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return print('A equação não possui raízes reais.')
    elif delta == 0:
        x = -b / (2*a)
        return print(f'A raiz única da equação de 2º grau é x = {x}.')
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return print(f'As raízes reais da equação de 2º grau são x1 = {x1} e x2 = {x2}.')

for resultado in calcular_equacao():
    print(resultado)