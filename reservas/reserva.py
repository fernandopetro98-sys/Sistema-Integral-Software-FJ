
# Clase Reserva para el sistema Software FJ.

from datetime import datetime

from reservas.excepciones import (
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError
)

from configuracion_logs import registrar_evento, registrar_error


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    def __init__(self, codigo, cliente, servicio, duracion):

        # Validar el código de la reserva.
        if not isinstance(codigo, str) or not codigo.strip():
            raise ReservaNoValidaError(
                "El código de la reserva no puede estar vacío."
            )

        # Validar la existencia del cliente.
        if cliente is None:
            raise ClienteNoEncontradoError(
                "No se puede crear una reserva sin un cliente."
            )

        # Validar la existencia del servicio.
        if servicio is None:
            raise ServicioNoDisponibleError(
                "No se puede crear una reserva sin un servicio."
            )

        # Validar la duración.
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ReservaNoValidaError(
                "La duración de la reserva debe ser mayor que cero."
            )

        # Almacenar los datos de la reserva.
        self._codigo = codigo.strip()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._fecha = datetime.now()

        # Registrar la creación de la reserva.
        registrar_evento(
            f"Se creó la reserva {self._codigo} "
            f"para el cliente {self._cliente.nombre}."
        )

    # Propiedades para acceder a los atributos privados.

    @property
    def codigo(self):
        return self._codigo

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def fecha(self):
        return self._fecha

    # Confirmar una reserva.

    def confirmar(self):
        """Confirma una reserva que se encuentra pendiente."""

        if self._estado != "Pendiente":
            raise ReservaNoValidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"

        registrar_evento(
            f"La reserva {self._codigo} fue confirmada."
        )

        return "La reserva ha sido confirmada correctamente."

    # Cancelar una reserva.

    def cancelar(self):
        """Cancela una reserva que todavía no ha sido procesada."""

        if self._estado == "Procesada":
            raise ReservaNoValidaError(
                "No se puede cancelar una reserva procesada."
            )

        if self._estado == "Cancelada":
            raise ReservaNoValidaError(
                "La reserva ya se encuentra cancelada."
            )

        self._estado = "Cancelada"

        registrar_evento(
            f"La reserva {self._codigo} fue cancelada."
        )

        return "La reserva ha sido cancelada correctamente."

    # Procesar una reserva.

    def procesar(self):
        """Procesa una reserva confirmada y calcula su costo."""

        if self._estado != "Confirmada":
            raise ReservaNoValidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            costo = self._servicio.calcular_costo(
                self._duracion
            )

        except (ValueError, TypeError) as error:

            registrar_error(
                f"Error al procesar la reserva "
                f"{self._codigo}: {error}"
            )

            raise ReservaNoValidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

        else:
            self._estado = "Procesada"

            registrar_evento(
                f"La reserva {self._codigo} fue procesada. "
                f"Costo total: ${costo:,.2f}"
            )

            return costo

        finally:
            print(
                f"Finalizó el intento de procesamiento "
                f"de la reserva {self._codigo}."
            )

    # Describir la reserva.

    def describir(self):
        """Devuelve la información general de la reserva."""

        return (
            f"Reserva: {self._codigo} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duración: {self._duracion} horas | "
            f"Estado: {self._estado} | "
            f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M')}"
        )
