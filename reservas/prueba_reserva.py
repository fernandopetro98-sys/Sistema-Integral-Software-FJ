# Prueba de creación, confirmación y procesamiento de reservas.

from entidades.cliente import Cliente
from servicios.sala import ReservaSala
from reservas.reserva import Reserva


print("====================================")
print("       PRUEBA DE RESERVA EXITOSA")
print("====================================")

try:
    # 1. Crear un cliente.
    cliente = Cliente(
        "C005",
        "Andrea Martinez",
        "andrea@gmail.com",
        "3201234567"
    )

    print("\nCliente creado correctamente.")

    # 2. Crear un servicio.
    servicio = ReservaSala(
        "S005",
        "Sala de conferencias",
        50000,
        20
    )

    print("Servicio creado correctamente.")

    # 3. Crear una reserva.
    reserva = Reserva(
        "R005",
        cliente,
        servicio,
        3
    )

    print("\nReserva creada:")
    print(reserva.describir())

    # 4. Confirmar la reserva.
    print("\nConfirmando reserva...")
    print(reserva.confirmar())

    # 5. Procesar la reserva.
    print("\nProcesando reserva...")
    costo = reserva.procesar()

    print(f"Costo total: ${costo:,.2f}")

    # 6. Mostrar el estado final.
    print("\nInformación final:")
    print(reserva.describir())

except Exception as error:
    print("\nSe presentó un error durante la prueba:")
    print(error)

print("\nPrueba finalizada.")