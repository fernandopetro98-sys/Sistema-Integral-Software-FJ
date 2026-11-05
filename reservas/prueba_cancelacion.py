# Prueba de cancelación de reservas.

from entidades.cliente import Cliente
from servicios.sala import ReservaSala
from reservas.reserva import Reserva


print("====================================")
print("       PRUEBA DE CANCELACIÓN")
print("====================================")

try:
    # Crear un cliente.
    cliente = Cliente(
        "C003",
        "Laura Gomez",
        "laura@gmail.com",
        "3101234567"
    )

    # Crear un servicio.
    servicio = ReservaSala(
        "S002",
        "Sala de capacitaciones",
        40000,
        15
    )

    # Crear una reserva.
    reserva = Reserva(
        "R002",
        cliente,
        servicio,
        2
    )

    print("\nReserva creada:")
    print(reserva.describir())

    # Confirmar la reserva.
    print("\nConfirmando reserva...")
    print(reserva.confirmar())

    # Procesar la reserva.
    print("\nProcesando reserva...")
    print("Costo:", reserva.procesar())

    # Intentar cancelar una reserva procesada.
    print("\nIntentando cancelar una reserva procesada...")

    try:
        reserva.cancelar()

    except Exception as error:
        print("El sistema impidió la cancelación.")
        print("Motivo:", error)

    print("\nEstado final:", reserva.estado)

except Exception as error:
    print("\nSe presentó un error:")
    print(error)