# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# Solicita o texto ao usuário
texto = input("Digite o texto que deseja repetir: ")

# Solicita o número e converte para inteiro (int)
# Usamos o try/except para evitar erros caso o usuário não digite um número
try:
    quantidade = int(input("Digite a quantidade de vezes: "))

    # Multiplica o texto pela quantidade
    # Adicionamos um espaço " " para que as palavras não fiquem grudadas
    resultado = (texto + "\n") * quantidade

    print("\nResultado: \n")
    print(resultado)

except ValueError:
    print("Por favor, digite um número inteiro válido para a quantidade.")