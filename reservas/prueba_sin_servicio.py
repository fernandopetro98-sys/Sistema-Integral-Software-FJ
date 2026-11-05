# Prueba de reserva sin servicio.

from entidades.cliente import Cliente
from reservas.reserva import Reserva


print("==============================")
print(" PRUEBA DE RESERVA SIN SERVICIO")
print("==============================")

try:
    cliente = Cliente(
        "C005",
        "Andres Perez",
        "andres@gmail.com",
        "3001234567"
    )

    reserva = Reserva(
        "R005",
        cliente,
        None,
        2
    )

    print(reserva.describir())

except Exception as error:
    print("\nEl sistema detectó correctamente el error.")
    print("Motivo:", error)