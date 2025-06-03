texto = "Aprendiendo Python con entusiasmo"

# 1. .title() – Convierte la primera letra de cada palabra a mayúscula
print(texto.title())  # Aprendiendo Python Con Entusiasmo

# 2. .startswith() – Verifica si una cadena comienza con un texto
print(texto.startswith("Aprendiendo"))  # True

# 3. .count() – Cuenta cuántas veces aparece una subcadena
print(texto.count("n"))  # 3

# 4. .find() – Devuelve el índice de la primera aparición de una subcadena
print(texto.find("Python"))  # 13

# 5. .replace() – Reemplaza una subcadena por otra
print(texto.replace("entusiasmo", "alegría"))  # aprendiendo Python con alegría