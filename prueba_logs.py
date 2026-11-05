
# Prueba del sistema de registro de eventos y errores.

from configuracion_logs import registrar_evento, registrar_error

print("====================================")
print("   PRUEBA DEL SISTEMA DE LOGS")
print("====================================")

registrar_evento("El sistema Software FJ se inició correctamente.")

registrar_evento("Se registró un nuevo cliente.")

registrar_error("Se presentó un error de prueba en el sistema.")

print("\nLos eventos y errores fueron registrados.")
print("Revisa el archivo sistema.log.")
