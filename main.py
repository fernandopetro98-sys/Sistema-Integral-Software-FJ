
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES,
# SERVICIOS Y RESERVAS - SOFTWARE FJ.

from entidades.cliente import Cliente
from servicios.sala import ReservaSala
from servicios.equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from reservas.reserva import Reserva
from reservas.excepciones import (
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError
)
from configuracion_logs import registrar_evento, registrar_error


def mostrar_titulo():
    print("=" * 60)
    print("       SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 60)


def registrar_cliente(clientes, identificador, nombre, correo, telefono):
    try:
        cliente = Cliente(identificador, nombre, correo, telefono)
        clientes.append(cliente)
        registrar_evento(f"Cliente {nombre} registrado correctamente.")
        print(f"Cliente registrado: {nombre}")
        return cliente

    except ValueError as error:
        registrar_error(f"Error al registrar cliente: {error}")
        print(f"Error al registrar cliente: {error}")
        return None


def crear_reserva(reservas, codigo, cliente, servicio, duracion):
    try:
        reserva = Reserva(codigo, cliente, servicio, duracion)
        reservas.append(reserva)
        print(reserva.describir())
        return reserva

    except (
        ClienteNoEncontradoError,
        ServicioNoDisponibleError,
        ReservaNoValidaError,
        ValueError
    ) as error:
        registrar_error(f"Error al crear reserva {codigo}: {error}")
        print(f"No fue posible crear la reserva: {error}")
        return None


def procesar_reserva(reserva):
    if reserva is None:
        return

    try:
        print(reserva.confirmar())
        costo = reserva.procesar()
        print(f"Costo total: ${costo:,.2f}")

    except ReservaNoValidaError as error:
        registrar_error(f"Error al procesar reserva: {error}")
        print(f"No fue posible procesar la reserva: {error}")


def ejecutar_sistema():
    mostrar_titulo()

    clientes = []
    servicios = []
    reservas = []

    registrar_evento("El sistema Software FJ se inició correctamente.")

    print("\n1. REGISTRO DE CLIENTES")

    cliente1 = registrar_cliente(
        clientes, "C001", "Maria Lopez",
        "maria@gmail.com", "3001234567"
    )

    cliente2 = registrar_cliente(
        clientes, "C002", "Laura Gomez",
        "laura@gmail.com", "3101234567"
    )

    cliente3 = registrar_cliente(
        clientes, "C003", "Andres Martinez",
        "andres@gmail.com", "3201234567"
    )

    # Prueba de cliente con correo incorrecto.
    registrar_cliente(
        clientes, "C004", "Carlos Perez",
        "correo_incorrecto", "3001234567"
    )

    print("\n2. CREACIÓN DE SERVICIOS")

    try:
        sala = ReservaSala(
            "S001", "Sala de capacitaciones", 40000, 15
        )

        equipo = AlquilerEquipo(
            "E001", "Equipo audiovisual", 30000, 5
        )

        asesoria = Asesoria(
            "A001", "Asesoria empresarial",
            60000, "Administración de empresas"
        )

        servicios.extend([sala, equipo, asesoria])

        for servicio in servicios:
            print(servicio.describir())

    except (ValueError, TypeError) as error:
        registrar_error(f"Error al crear servicios: {error}")
        print(f"Error al crear servicios: {error}")
        return

    print("\n3. CREACIÓN Y PROCESAMIENTO DE RESERVAS")

    reserva1 = crear_reserva(
        reservas, "R001", cliente1, sala, 2
    )
    procesar_reserva(reserva1)

    reserva2 = crear_reserva(
        reservas, "R002", cliente2, equipo, 3
    )
    procesar_reserva(reserva2)

    reserva3 = crear_reserva(
        reservas, "R003", cliente3, asesoria, 2
    )
    procesar_reserva(reserva3)

    print("\n4. PRUEBAS DE OPERACIONES NO VÁLIDAS")

    # Reserva con duración incorrecta.
    crear_reserva(
        reservas, "R004", cliente1, sala, 0
    )

    # Reserva sin cliente.
    crear_reserva(
        reservas, "R005", None, sala, 2
    )

    # Reserva sin servicio.
    crear_reserva(
        reservas, "R006", cliente2, None, 2
    )

    print("\n5. PRUEBA DE CANCELACIÓN")

    reserva_cancelable = crear_reserva(
        reservas, "R007", cliente1, equipo, 1
    )

    if reserva_cancelable is not None:
        try:
            print(reserva_cancelable.cancelar())

        except ReservaNoValidaError as error:
            registrar_error(f"Error al cancelar reserva: {error}")
            print(error)

    print("\n6. RESUMEN DEL SISTEMA")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas correctamente: {len(reservas)}")

    for reserva in reservas:
        print(reserva.describir())

    registrar_evento("La ejecución del sistema finalizó correctamente.")

    print("\nSistema Software FJ ejecutado.")
    print("Consulta sistema.log para revisar los eventos y errores.")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_sistema()
