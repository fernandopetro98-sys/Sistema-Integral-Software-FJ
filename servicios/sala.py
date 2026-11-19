# Servicio especializado para la reserva de salas.

from servicios.servicio import Servicio, es_entero_positivo


class ReservaSala(Servicio):
    """Representa el servicio de reserva de salas ofrecido por Software FJ."""

    def __init__(self, codigo, nombre, tarifa, capacidad):
        if not es_entero_positivo(capacidad):
            raise ValueError("La capacidad debe ser un entero positivo.")

        super().__init__(codigo, nombre, tarifa)
        self._capacidad = capacidad

    @property
    def capacidad(self):
        return self._capacidad

    def describir(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Tarifa por hora: ${self.tarifa:,.2f} | "
            f"Capacidad: {self._capacidad} personas"
        )
