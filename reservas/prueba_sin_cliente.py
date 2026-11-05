# Prueba de reserva sin cliente.

from servicios.sala import ReservaSala
from reservas.reserva import Reserva


print("==============================")
print(" PRUEBA DE RESERVA SIN CLIENTE")
print("==============================")

try:
    servicio = ReservaSala(
        "S004",
        "Sala principal",
        50000,
        20
    )

    reserva = Reserva(
        "R004",
        None,
        servicio,
        2
    )

    print(reserva.describir())

except Exception as error:
    print("\nEl sistema detectó correctamente el error.")
    print("Motivo:", error)