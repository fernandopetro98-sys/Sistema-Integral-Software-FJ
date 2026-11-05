# Prueba de excepciones personalizadas.

from reservas.excepciones import (
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaNoValidaError
)


print("====================================")
print(" PRUEBA DE EXCEPCIONES PERSONALIZADAS")
print("====================================")


# 1. Probar la excepción de cliente.

try:
    raise ClienteNoEncontradoError(
        "No se encontró el cliente solicitado."
    )

except ClienteNoEncontradoError as error:
    print("\nExcepción de cliente:")
    print(error)


# 2. Probar la excepción de servicio.

try:
    raise ServicioNoDisponibleError(
        "El servicio solicitado no está disponible."
    )

except ServicioNoDisponibleError as error:
    print("\nExcepción de servicio:")
    print(error)


# 3. Probar la excepción de reserva.

try:
    raise ReservaNoValidaError(
        "La reserva no cumple los requisitos."
    )

except ReservaNoValidaError as error:
    print("\nExcepción de reserva:")
    print(error)


print("\nLas excepciones personalizadas funcionan correctamente.")