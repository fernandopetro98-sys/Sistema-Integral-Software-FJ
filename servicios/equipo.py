# Servicio especializado para el alquiler de equipos.

from servicios.servicio import Servicio


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos
    ofrecido por la empresa Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa, cantidad_disponible):
        super().__init__(codigo, nombre, tarifa)

        if (
            not isinstance(cantidad_disponible, int)
            or isinstance(cantidad_disponible, bool)
            or cantidad_disponible <= 0
        ):
            raise ValueError(
                "La cantidad disponible debe ser un entero positivo."
            )

        self._cantidad_disponible = cantidad_disponible

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    def validar_parametros(self, duracion):
        """Valida la duración del alquiler."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del alquiler según su duración."""

        self.validar_parametros(duracion)

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not 0 <= impuesto <= 1
        ):
            raise ValueError("El impuesto debe estar entre 0 y 1.")

        if (
            not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
            or not 0 <= descuento <= 1
        ):
            raise ValueError("El descuento debe estar entre 0 y 1.")

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto)
        total = total - (total * descuento)

        return round(total, 2)

    def describir(self):
        """Devuelve la descripción del servicio de alquiler."""

        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Tarifa por hora: ${self.tarifa:,.2f} | "
            f"Equipos disponibles: {self._cantidad_disponible}"
        )