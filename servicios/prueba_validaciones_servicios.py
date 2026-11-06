
from servicios.sala import ReservaSala
from servicios.equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from configuracion_logs import registrar_evento, registrar_error


def probar_validaciones():
    pruebas = [
        ("Sala con capacidad cero",
         lambda: ReservaSala("S01", "Sala", 50000, 0)),

        ("Equipo con cantidad negativa",
         lambda: AlquilerEquipo("E01", "Proyector", 30000, -2)),

        ("Asesoría sin especialidad",
         lambda: Asesoria("A01", "Asesoría", 60000, "")),

        ("Servicio con tarifa cero",
         lambda: ReservaSala("S02", "Sala", 0, 10)),

        ("Duración negativa",
         lambda: ReservaSala("S03", "Sala", 50000, 10).calcular_costo(-2)),

        ("Impuesto superior a 1",
         lambda: ReservaSala("S04", "Sala", 50000, 10).calcular_costo(2, impuesto=1.5)),

        ("Descuento negativo",
         lambda: Asesoria("A02", "Asesoría", 60000, "Administración").calcular_costo(2, descuento=-0.5)),
    ]

    exitos = 0

    print("=" * 55)
    print("PRUEBAS DE VALIDACIÓN - SOFTWARE FJ")
    print("=" * 55)

    registrar_evento("Inicio de pruebas de validación de servicios.")

    for nombre, prueba in pruebas:
        try:
            prueba()

        except (ValueError, TypeError) as error:
            print(f"[CORRECTO] {nombre}: dato inválido rechazado.")

            registrar_error(
                f"Validación correcta - {nombre}. Motivo: {error}"
            )

            exitos += 1

        else:
            mensaje = (
                f"ERROR: {nombre}. "
                "El sistema aceptó un dato inválido."
            )

            print(f"[ERROR] {nombre}: el dato inválido fue aceptado.")
            registrar_error(mensaje)

    print("=" * 55)
    print(f"Pruebas superadas: {exitos} de {len(pruebas)}")
    print("=" * 55)

    registrar_evento(
        f"Finalizaron las pruebas de validación. "
        f"Resultados: {exitos} de {len(pruebas)}."
    )


if __name__ == "__main__":
    probar_validaciones()
