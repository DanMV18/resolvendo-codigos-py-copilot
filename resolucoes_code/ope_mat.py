# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe as opções de operação
print("\nEscolha a operação:")
print("+ : Soma")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")

operacao = input("\nDigite a operação desejada: ")

# Realiza o cálculo baseado na escolha
if operacao == "soma":
    resultado = num1 + num2
    print(f"\nResultado: {num1} + {num2} = {resultado}")
elif operacao == "subtração":
    resultado = num1 - num2
    print(f"\nResultado: {num1} - {num2} = {resultado}")
elif operacao == "multiplicação":
    resultado = num1 * num2
    print(f"\nResultado: {num1} * {num2} = {resultado}")
elif operacao == "divisão":
    # Verifica se o usuário não está tentando dividir por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero!")
else:
    print("\nOperação inválida. Por favor, tente novamente.")