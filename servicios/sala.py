
# Servicio especializado para la reserva de salas.

from servicios.servicio import Servicio


class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de salas
    ofrecido por Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa, capacidad):

        # Validar la capacidad de la sala.
        if (
            not isinstance(capacidad, int)
            or isinstance(capacidad, bool)
            or capacidad <= 0
        ):
            raise ValueError(
                "La capacidad debe ser un entero positivo."
            )

        super().__init__(codigo, nombre, tarifa)

        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    def validar_parametros(self, duracion):
        """Valida la duración de la reserva."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError(
                "La duración debe ser mayor que cero."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo de la reserva de sala."""

        self.validar_parametros(duracion)

        # Validar el impuesto.
        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 1
        ):
            raise ValueError(
                "El impuesto debe estar entre 0 y 1."
            )

        # Validar el descuento.
        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 1
        ):
            raise ValueError(
                "El descuento debe estar entre 0 y 1."
            )

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto)
        total = total - (total * descuento)

        return round(total, 2)

    def describir(self):
        """Devuelve la descripción de la sala."""

        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Tarifa por hora: ${self.tarifa:,.2f} | "
            f"Capacidad: {self._capacidad} personas"
        )
