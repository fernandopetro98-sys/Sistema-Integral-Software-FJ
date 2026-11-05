# Prueba del servicio de alquiler de equipos.

from servicios.equipo import AlquilerEquipo

print("====================================")
print("   PRUEBA DEL SERVICIO DE EQUIPOS")
print("====================================")

try:
    equipo = AlquilerEquipo(
        "E001",
        "Computador portátil",
        30000,
        10
    )

    print("\nServicio creado correctamente.")
    print(equipo.describir())

    costo = equipo.calcular_costo(3)

    print("\nCosto del alquiler por 3 horas:")
    print(f"${costo:,.2f}")

    print("\nPrueba finalizada.")

except ValueError as error:
    print("Se presentó un error:", error)