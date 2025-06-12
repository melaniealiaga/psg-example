# Ejercicio 3
pregunta = tuple(input("Escribe una pregunta: "))

resultado = ('¿',) + pregunta + ('?',)
print("Tupla concatenada:", resultado)

repetida = resultado * 2
print("Tupla repetida:", repetida)