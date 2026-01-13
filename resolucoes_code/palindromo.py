def eh_palindromo(texto):
    # Remove espaços e transforma tudo em minúsculo
    texto_limpo = texto.replace(" ", "").lower()
    
    # Inverte a string usando fatiamento (slicing)
    texto_invertido = texto_limpo[::-1]
    
    # Compara a string original limpa com a invertida
    return texto_limpo == texto_invertido

# Entrada do usuário
entrada = input("Digite uma palavra ou frase: ")

if eh_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo!')
else:
    print(f'"{entrada}" não é um palíndromo.')