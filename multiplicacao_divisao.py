# Função para Multiplicação
n = int(input('Digite um número: '))
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')


# Função de divisão
# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica se o segundo número é diferente de zero
if num2 != 0:
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)
else:
    print("Erro: divisão por zero não é permitida.")