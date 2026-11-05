# Servicio especializado para el alquiler de equipos.

from servicios.servicio import Servicio


class AlquilerEquipo(Servicio):
    """
    Representa el servicio de alquiler de equipos
    ofrecido por la empresa Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa, cantidad_disponible):
        super().__init__(codigo, nombre, tarifa)

        if not isinstance(cantidad_disponible, int) or isinstance(cantidad_disponible, bool) or cantidad_disponible <= 0:
            raise ValueError("La cantidad disponible debe ser un entero positivo.")

        self._cantidad_disponible = cantidad_disponible

    def validar_parametros(self, duracion):
        """Valida la duración del alquiler."""

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del alquiler según su duración."""

        self.validar_parametros(duracion)

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