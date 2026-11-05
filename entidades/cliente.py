
# Clase Cliente para el sistema Software FJ.

import re
from entidades.entidad import Entidad


class Cliente(Entidad):
    """
    Representa a un cliente registrado en Software FJ.
    Hereda los atributos y métodos de la clase Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        # Inicializa el identificador heredado.
        super().__init__(identificador)

        # Valida y almacena los datos personales.
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not isinstance(valor, str) or not re.match(patron, valor.strip()):
            raise ValueError("El correo electrónico no es válido.")

        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not valor.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        if len(valor) != 10:
            raise ValueError("El teléfono debe tener 10 dígitos.")

        self._telefono = valor

    def describir(self):
        """Devuelve la información del cliente."""

        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
