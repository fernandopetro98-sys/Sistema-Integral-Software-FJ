# Prueba para impedir el procesamiento de una reserva pendiente.

from entidades.cliente import Cliente
from servicios.sala import ReservaSala
from reservas.reserva import Reserva
from reservas.excepciones import ReservaNoValidaError


def probar_procesamiento_pendiente():

    print("=" * 45)
    print(" PRUEBA DE PROCESAMIENTO SIN CONFIRMAR")
    print("=" * 45)

    cliente = Cliente(
        "C010",
        "Sofia Perez",
        "sofia@gmail.com",
        "3001234567"
    )

    servicio = ReservaSala(
        "S010",
        "Sala de reuniones",
        50000,
        10
    )

    reserva = Reserva(
        "R010",
        cliente,
        servicio,
        2
    )

    print("\nEstado inicial:", reserva.estado)

    try:
        reserva.procesar()

    except ReservaNoValidaError as error:
        print("\nEl sistema detectó correctamente el error.")
        print("Motivo:", error)
        print("Estado final:", reserva.estado)

    else:
        print("\nERROR: El sistema permitió procesar una reserva pendiente.")


if __name__ == "__main__":
    probar_procesamiento_pendiente()