def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

texto = input("Ingresa una frase: ")
print("¿Es palíndromo?:", es_palindromo(texto))