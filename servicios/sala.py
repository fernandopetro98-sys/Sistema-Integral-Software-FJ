# Servicio especializado para la reserva de salas.

from servicios.servicio import Servicio


class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de salas
    ofrecido por Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa, capacidad):
        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un entero positivo.")

        super().__init__(codigo, nombre, tarifa)
        self._capacidad = capacidad

    def validar_parametros(self, duracion):
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto)
        total = total - (total * descuento)

        return round(total, 2)

    def describir(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Tarifa por hora: ${self.tarifa:,.2f} | "
            f"Capacidad: {self._capacidad} personas"
        )