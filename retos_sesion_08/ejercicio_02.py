# Ejercicio 2
letras = ('a','b','c','d','e','f','g','h','i','j')

print("Primer elemento:", letras[0])       # 'a'
print("Último elemento:", letras[-1])      # 'j'
print("Slice del índice 3 al 5:", letras[3:6])        # 'd','e','f'
print("Slice del 5 al 9 con pasos de 3:", letras[5:10:3])  # 'f','i'
print("Slice del 9 al 0 con pasos de -2:", letras[9::-2])  # 'j','h','f','d','b'