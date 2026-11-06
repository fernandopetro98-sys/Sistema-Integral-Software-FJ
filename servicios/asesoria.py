# Servicio especializado de asesorías.

from servicios.servicio import Servicio


class Asesoria(Servicio):
    """
    Representa el servicio de asesorías especializadas
    ofrecido por Software FJ.
    """

    def __init__(self, codigo, nombre, tarifa, especialidad):
        super().__init__(codigo, nombre, tarifa)
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La especialidad no puede estar vacía.")

        self._especialidad = valor.strip()

    def validar_parametros(self, duracion):
        """Valida la duración de la asesoría."""

        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo de la asesoría."""

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
        """Devuelve la descripción de la asesoría."""

        return (
            f"Servicio: {self.nombre} | "
            f"Código: {self.codigo} | "
            f"Especialidad: {self.especialidad} | "
            f"Tarifa por hora: ${self.tarifa:,.2f}"
        )