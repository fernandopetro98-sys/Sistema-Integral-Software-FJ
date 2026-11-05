# Prueba del servicio de reserva de salas.

from servicios.sala import ReservaSala

print("====================================")
print("   PRUEBA DEL SERVICIO DE SALAS")
print("====================================")

try:
    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        50000,
        10
    )

    print("\nServicio creado correctamente.")
    print(sala.describir())

    costo = sala.calcular_costo(2)

    print("\nCosto de reserva por 2 horas:")
    print(f"${costo:,.2f}")

except ValueError as error:
    print("\nEl sistema detectó un error:")
    print(error)

print("\nPrueba finalizada.")