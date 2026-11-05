# Servicio especializado de asesorías.

from servicios.servicio import Servicio


class Asesoria(Servicio):
    """
    Representa el servicio de asesorías especializadas
    ofrecido por Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa, especialidad):
        super().__init__(codigo, nombre, tarifa)
        self._especialidad = especialidad

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")

    def validar_parametros(self, duracion):
        """Valida la duración de la asesoría."""

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo de la asesoría."""

        self.validar_parametros(duracion)

        subtotal = self.tarifa * duracion
        total = subtotal + (subtotal * impuesto)
        total = total - (total * descuento)

        return round(total, 2)

    def describir(self):
        """Devuelve la descripción de la asesoría."""

        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Especialidad: {self._especialidad} | "
            f"Tarifa por hora: ${self.tarifa:,.2f}"
        )