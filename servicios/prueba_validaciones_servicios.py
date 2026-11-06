
from servicios.sala import ReservaSala
from servicios.equipo import AlquilerEquipo
from servicios.asesoria import Asesoria


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

    for nombre, prueba in pruebas:
        try:
            prueba()
        except (ValueError, TypeError):
            print(f"[CORRECTO] {nombre}: dato inválido rechazado.")
            exitos += 1
        else:
            print(f"[ERROR] {nombre}: el dato inválido fue aceptado.")

    print("=" * 55)
    print(f"Pruebas superadas: {exitos} de {len(pruebas)}")
    print("=" * 55)


if __name__ == "__main__":
    probar_validaciones()
