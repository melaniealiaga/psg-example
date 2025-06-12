# Ejercicio 4
notas = (10, 61, 0, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")

if promedio >= 51:
    print("¡Aprobado!")
else:
    print("Reprobado")
