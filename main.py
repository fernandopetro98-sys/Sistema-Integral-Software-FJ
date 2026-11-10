
# SISTEMA INTEGRAL DE GESTION DE CLIENTES,
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


# Listas que almacenan la informacion durante la ejecucion.
clientes = []
servicios = []
reservas = []


def mostrar_titulo():
    print("\n" + "=" * 60)
    print("       SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("=" * 60)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def buscar_cliente(identificador):
    for cliente in clientes:
        if cliente.identificador == identificador:
            return cliente
    return None


def buscar_servicio(codigo):
    for servicio in servicios:
        if servicio.codigo == codigo:
            return servicio
    return None


def buscar_reserva(codigo):
    for reserva in reservas:
        if reserva.codigo == codigo:
            return reserva
    return None


def registrar_cliente():
    print("\n--- REGISTRO DE CLIENTES ---")

    try:
        identificador = input("Identificacion: ").strip()

        if buscar_cliente(identificador):
            print("Ya existe un cliente con esa identificacion.")
            return

        nombre = input("Nombre completo: ").strip()
        correo = input("Correo electronico: ").strip()
        telefono = input("Telefono: ").strip()

        cliente = Cliente(
            identificador, nombre, correo, telefono
        )

        clientes.append(cliente)
        registrar_evento(
            f"Cliente {nombre} registrado correctamente."
        )

        print("\nCliente registrado exitosamente.")

    except (ValueError, TypeError) as error:
        registrar_error(f"Error al registrar cliente: {error}")
        print(f"No fue posible registrar el cliente: {error}")


def mostrar_clientes():
    print("\n--- CLIENTES REGISTRADOS ---")

    if not clientes:
        print("Todavia no hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente.describir())


def registrar_servicio():
    print("\n--- REGISTRO DE SERVICIOS ---")
    print("1. Reserva de sala")
    print("2. Alquiler de equipos")
    print("3. Asesoria especializada")

    opcion = leer_entero("Seleccione el tipo de servicio: ")

    if opcion not in (1, 2, 3):
        print("Opcion no valida.")
        return

    try:
        codigo = input("Codigo del servicio: ").strip()

        if buscar_servicio(codigo):
            print("Ya existe un servicio con ese codigo.")
            return

        nombre = input("Nombre del servicio: ").strip()
        tarifa = leer_entero("Tarifa del servicio: ")

        if opcion == 1:
            capacidad = leer_entero("Capacidad de la sala: ")
            servicio = ReservaSala(
                codigo, nombre, tarifa, capacidad
            )

        elif opcion == 2:
            cantidad = leer_entero("Cantidad de equipos disponibles: ")
            servicio = AlquilerEquipo(
                codigo, nombre, tarifa, cantidad
            )

        else:
            especialidad = input("Especialidad de la asesoria: ")
            servicio = Asesoria(
                codigo, nombre, tarifa, especialidad
            )

        servicios.append(servicio)

        registrar_evento(
            f"Servicio {nombre} registrado correctamente."
        )

        print("\nServicio registrado exitosamente.")

    except (ValueError, TypeError) as error:
        registrar_error(f"Error al registrar servicio: {error}")
        print(f"No fue posible registrar el servicio: {error}")


def mostrar_servicios():
    print("\n--- SERVICIOS DISPONIBLES ---")

    if not servicios:
        print("Todavia no hay servicios registrados.")
        return

    for servicio in servicios:
        print(servicio.describir())


def crear_reserva():
    print("\n--- CREAR RESERVA ---")

    if not clientes:
        print("Primero debe registrar un cliente.")
        return

    if not servicios:
        print("Primero debe registrar un servicio.")
        return

    try:
        print("\nCLIENTES:")
        mostrar_clientes()

        identificador = input(
            "\nIdentificacion del cliente: "
        ).strip()

        cliente = buscar_cliente(identificador)

        print("\nSERVICIOS:")
        mostrar_servicios()

        codigo_servicio = input(
            "\nCodigo del servicio: "
        ).strip()

        servicio = buscar_servicio(codigo_servicio)

        codigo_reserva = input(
            "Codigo de la reserva: "
        ).strip()

        if buscar_reserva(codigo_reserva):
            print("Ya existe una reserva con ese codigo.")
            return

        duracion = leer_entero("Duracion de la reserva: ")

        reserva = Reserva(
            codigo_reserva, cliente, servicio, duracion
        )

        reservas.append(reserva)

        registrar_evento(
            f"Reserva {codigo_reserva} creada correctamente."
        )

        print("\nReserva creada exitosamente.")
        print(reserva.describir())

    except (
        ClienteNoEncontradoError,
        ServicioNoDisponibleError,
        ReservaNoValidaError,
        ValueError,
        TypeError
    ) as error:
        registrar_error(f"Error al crear reserva: {error}")
        print(f"No fue posible crear la reserva: {error}")


def mostrar_reservas():
    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("Todavia no hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.describir())


def confirmar_reserva():
    print("\n--- CONFIRMAR RESERVA ---")

    codigo = input("Codigo de la reserva: ").strip()
    reserva = buscar_reserva(codigo)

    if reserva is None:
        print("No se encontro la reserva.")
        return

    try:
        print(reserva.confirmar())
        registrar_evento(f"Reserva {codigo} confirmada.")

    except ReservaNoValidaError as error:
        registrar_error(f"Error al confirmar reserva: {error}")
        print(f"No fue posible confirmar: {error}")


def cancelar_reserva():
    print("\n--- CANCELAR RESERVA ---")

    codigo = input("Codigo de la reserva: ").strip()
    reserva = buscar_reserva(codigo)

    if reserva is None:
        print("No se encontro la reserva.")
        return

    try:
        print(reserva.cancelar())
        registrar_evento(f"Reserva {codigo} cancelada.")

    except ReservaNoValidaError as error:
        registrar_error(f"Error al cancelar reserva: {error}")
        print(f"No fue posible cancelar: {error}")


def procesar_reserva():
    print("\n--- PROCESAR RESERVA ---")

    codigo = input("Codigo de la reserva: ").strip()
    reserva = buscar_reserva(codigo)

    if reserva is None:
        print("No se encontro la reserva.")
        return

    try:
        resultado = reserva.procesar()
        print(f"Reserva procesada correctamente.")
        print(f"Costo total: ${resultado:,.2f}")

        registrar_evento(f"Reserva {codigo} procesada.")

    except ReservaNoValidaError as error:
        registrar_error(f"Error al procesar reserva: {error}")
        print(f"No fue posible procesar la reserva: {error}")


def mostrar_menu():
    print("\n" + "=" * 50)
    print("                 MENU PRINCIPAL")
    print("=" * 50)
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Registrar servicio")
    print("4. Mostrar servicios")
    print("5. Crear reserva")
    print("6. Mostrar reservas")
    print("7. Confirmar reserva")
    print("8. Cancelar reserva")
    print("9. Procesar reserva")
    print("0. Salir")
    print("=" * 50)


def ejecutar_sistema():
    registrar_evento(
        "Sistema Software FJ iniciado."
    )

    mostrar_titulo()

    while True:
        mostrar_menu()

        opcion = leer_entero("Seleccione una opcion: ")

        if opcion == 1:
            registrar_cliente()

        elif opcion == 2:
            mostrar_clientes()

        elif opcion == 3:
            registrar_servicio()

        elif opcion == 4:
            mostrar_servicios()

        elif opcion == 5:
            crear_reserva()

        elif opcion == 6:
            mostrar_reservas()

        elif opcion == 7:
            confirmar_reserva()

        elif opcion == 8:
            cancelar_reserva()

        elif opcion == 9:
            procesar_reserva()

        elif opcion == 0:
            registrar_evento(
                "Sistema Software FJ finalizado."
            )
            print("\nGracias por utilizar Software FJ.")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_sistema()
