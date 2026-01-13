# Programa para calcular a média de três notas

print("--- Calculadora de Média ---")

# Solicitando as notas ao usuário
# Usamos float() para permitir números decimais (ex: 7.5)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média
media = (nota1 + nota2 + nota3) / 3

# Exibindo o resultado
# O :.2f formata o número para ter apenas duas casas decimais
print(f"\nA média final é: {media:.2f}")

# Uma estrutura de decisão simples para dar um feedback
if media >= 7:
    print("Status: Aprovado!")
else:
    print("Status: Recuperação.")