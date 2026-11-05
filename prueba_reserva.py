# Prueba inicial del sistema de reservas Software FJ.

from entidades.cliente import Cliente
from servicios.sala import ReservaSala
from reservas.reserva import Reserva


print("======================================")
print("       PRUEBA DEL SISTEMA DE RESERVAS")
print("======================================")

try:
    # Crear un cliente.
    cliente = Cliente(
        "C001",
        "Maria Lopez",
        "maria@gmail.com",
        "3001234567"
    )

    # Crear un servicio de reserva de sala.
    servicio = ReservaSala(
        "S001",
        "Sala de reuniones",
        50000,
        20
    )

    # Crear la reserva.
    reserva = Reserva(
        "R001",
        cliente,
        servicio,
        2
    )

    print("\nReserva creada correctamente.")
    print(reserva.describir())

    # Confirmar la reserva.
    print("\n" + reserva.confirmar())
    print("Estado actual:", reserva.estado)
    # Procesar la reserva.
    print("\nProcesando la reserva...")

    costo = reserva.procesar()

    print("Costo total del servicio: $", costo)
    print("Estado final:", reserva.estado)

except Exception as error:
    print("\nSe presentó un error:")
    print(error)