# Prueba del servicio de asesorías especializadas.

from servicios.asesoria import Asesoria

print("======================================")
print("   PRUEBA DEL SERVICIO DE ASESORÍA")
print("======================================")

try:
    # Crear un servicio de asesoría.
    asesoria = Asesoria(
        "S004",
        "Asesoría empresarial",
        60000,
        "Administración de empresas"
    )

    print("\nServicio creado correctamente.")
    print(asesoria.describir())

    # Validar la duración.
    print("\nValidando duración...")
    asesoria.validar_parametros(2)
    print("La duración es válida.")

    # Calcular el costo.
    print("\nCalculando costo...")
    costo = asesoria.calcular_costo(2)

    print("Duración: 2 horas")
    print("Costo total: $", costo)

except ValueError as error:
    print("\nEl sistema detectó un error:")
    print(error)

except Exception as error:
    print("\nSe presentó un error inesperado:")
    print(error)