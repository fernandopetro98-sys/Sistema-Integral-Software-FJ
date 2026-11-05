# Excepciones personalizadas del sistema Software FJ.


class ErrorReserva(Exception):
    """Excepción general relacionada con las reservas."""

    def __init__(self, mensaje="Se presentó un error en el sistema de reservas."):
        super().__init__(mensaje)


class ClienteNoEncontradoError(ErrorReserva):
    """Se genera cuando no se encuentra un cliente."""

    def __init__(self, mensaje="El cliente no se encuentra registrado."):
        super().__init__(mensaje)


class ServicioNoDisponibleError(ErrorReserva):
    """Se genera cuando un servicio no está disponible."""

    def __init__(self, mensaje="El servicio solicitado no está disponible."):
        super().__init__(mensaje)


class ReservaNoValidaError(ErrorReserva):
    """Se genera cuando una reserva no cumple los requisitos."""

    def __init__(self, mensaje="La reserva no cumple con los requisitos establecidos."):
        super().__init__(mensaje)