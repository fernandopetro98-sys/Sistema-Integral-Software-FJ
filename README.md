
# Sistema Integral de Gestión - Software FJ

## 1. Descripción del proyecto

Sistema Integral de Gestión de Clientes, Servicios y Reservas, desarrollado en Python mediante programación orientada a objetos para la empresa Software FJ.

El sistema permite registrar clientes, administrar servicios y gestionar reservas de manera organizada, aplicando validaciones y manejo de excepciones.

## 2. Objetivo

Desarrollar una solución de software que permita gestionar clientes, servicios y reservas, aplicando los principios fundamentales de la programación orientada a objetos.

## 3. Funcionalidades principales

- Registro y validación de clientes.
- Gestión de reservas de salas.
- Alquiler de equipos.
- Gestión de asesorías especializadas.
- Creación, confirmación, procesamiento y cancelación de reservas.
- Cálculo automático de costos.
- Validación de datos y operaciones.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores mediante archivos de logs.

## 4. Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos.
- Módulo logging.
- Módulo datetime.
- Módulo abc.
- Módulo re.
- Git y GitHub.

## 5. Estructura del proyecto

```text
SOFTWARE_FJ/
│
├── entidades/
│   ├── entidad.py
│   └── cliente.py
│
├── servicios/
│   ├── servicio.py
│   ├── sala.py
│   ├── equipo.py
│   ├── asesoria.py
│   └── pruebas de servicios
│
├── reservas/
│   ├── reserva.py
│   ├── excepciones.py
│   └── pruebas de reservas
│
├── configuracion_logs.py
├── main.py
├── prueba_logs.py
├── prueba_reserva.py
├── sistema.log
└── README.md
```

## 6. Principios de programación orientada a objetos

El proyecto implementa:

- **Abstracción:** mediante las clases abstractas Entidad y Servicio.
- **Herencia:** mediante las clases Cliente, ReservaSala, AlquilerEquipo y Asesoria.
- **Encapsulamiento:** mediante atributos privados y propiedades.
- **Polimorfismo:** mediante la implementación de métodos especializados como describir() y calcular_costo().

## 7. Manejo de excepciones

El sistema incorpora excepciones personalizadas para controlar errores relacionados con clientes, servicios y reservas.

También utiliza estructuras try, except, else y finally, además del encadenamiento de excepciones.

## 8. Registro de eventos

Se utiliza el módulo logging de Python para almacenar eventos y errores en el archivo sistema.log.

## 9. Requisitos de ejecución

- Tener Python 3 instalado.
- Contar con Visual Studio Code o una terminal compatible.
- Descargar o clonar el repositorio del proyecto.

## 10. Ejecución del sistema

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

## 11. Pruebas

El proyecto incluye pruebas para verificar:

- Registro de clientes válidos e inválidos.
- Creación de servicios.
- Cálculo de costos.
- Creación y procesamiento de reservas.
- Validación de operaciones no permitidas.
- Excepciones personalizadas.
- Cancelación de reservas.
- Registro de eventos y errores.

## 12. Repositorio

Código fuente del proyecto:

https://github.com/fernandopetro98-sys/Sistema-Integral-Software-FJ.git

## 13. Autoría

Proyecto académico desarrollado colaborativamente por el equipo de trabajo.
