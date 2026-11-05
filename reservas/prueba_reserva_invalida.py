# Prueba de validación de reservas inválidas.

from entidades.cliente import Cliente
from servicios.sala import ReservaSala
from reservas.reserva import Reserva

print("====================================")
print("   PRUEBA DE RESERVA NO VALIDA")
print("====================================")

try:
    cliente = Cliente(
        "C004",
        "Carlos Perez",
        "carlos@gmail.com",
        "3001234567"
    )

    servicio = ReservaSala(
        "S003",
        "Sala principal",
        50000,
        20
    )

    # Intentar crear una reserva con duración cero.
    reserva = Reserva(
        "R003",
        cliente,
        servicio,
        0
    )

    print(reserva.describir())

except Exception as error:
    print("\nEl sistema detectó correctamente el error.")
    print("Motivo:", error)