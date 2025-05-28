# Ejercicio 03
print("Tarjeta | Huella | Puerta se abre")
for tarjeta in [True, False]:
    for huella in [True, False]:
        puerta = tarjeta ^ huella  # XOR lógico
        print(f"  {tarjeta}   |  {huella}  |     {puerta}")