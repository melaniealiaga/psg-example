# Ejercicio 03
# Total de segundos
segundos_totales = 1000000

# Conversión
semanas = segundos_totales // (7 * 24 * 3600)
resto = segundos_totales % (7 * 24 * 3600)

días = resto // (24 * 3600)
resto %= (24 * 3600)

horas = resto // 3600
resto %= 3600

minutos = resto // 60
segundos = resto % 60

# Mostrar resultado
print(f"{segundos_totales} segundos = {semanas} semanas {días} días {horas} horas {minutos} minutos {segundos} segundos")