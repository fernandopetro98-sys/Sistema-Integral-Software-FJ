# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción del proyecto

El Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ es una aplicación desarrollada en Python mediante programación orientada a objetos.

Su propósito es facilitar la gestión de clientes, servicios y reservas de una empresa, mediante una estructura modular que permite registrar información, administrar servicios especializados, calcular costos y controlar las operaciones de reserva.

El sistema trabaja con listas en memoria y no utiliza un motor de base de datos.

## 2. Objetivo

Desarrollar una solución de software que permita gestionar clientes, servicios y reservas, aplicando los principios fundamentales de la programación orientada a objetos, validaciones, excepciones personalizadas y registro de eventos y errores.

## 3. Funcionalidades principales

- Registro y validación de clientes.
- Gestión de reservas de salas.
- Alquiler de equipos.
- Gestión de asesorías especializadas.
- Creación, confirmación, procesamiento y cancelación de reservas.
- Cálculo automático de costos.
- Validación de datos y operaciones.
- Manejo de excepciones personalizadas.
- Control de estados de las reservas.
- Registro de eventos y errores mediante archivos de logs.
- Ejecución de pruebas para comprobar operaciones válidas e inválidas.

## 4. Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos.
- Módulo `abc`.
- Módulo `logging`.
- Módulo `datetime`.
- Módulo `re`.
- Git.
- GitHub.
- Visual Studio Code como entorno de desarrollo.

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
│   ├── prueba_sala.py
│   ├── prueba_equipo.py
│   ├── prueba_asesoria.py
│   └── prueba_validaciones_servicios.py
│
├── reservas/
│   ├── excepciones.py
│   ├── reserva.py
│   ├── prueba_cancelacion.py
│   ├── prueba_excepciones.py
│   ├── prueba_procesamiento_pendiente.py
│   ├── prueba_reserva.py
│   ├── prueba_reserva_invalida.py
│   ├── prueba_sin_cliente.py
│   └── prueba_sin_servicio.py
│
├── configuracion_logs.py
├── main.py
├── prueba_logs.py
├── prueba_reserva.py
├── .gitignore
└── README.md
```

## 6. Principios de programación orientada a objetos

El proyecto implementa los siguientes principios:

- **Abstracción:** mediante las clases abstractas `Entidad` y `Servicio`.
- **Herencia:** mediante clases especializadas que heredan de las clases base correspondientes.
- **Encapsulamiento:** mediante atributos protegidos y propiedades que permiten controlar el acceso a los datos.
- **Polimorfismo:** mediante la implementación especializada de métodos como `describir()` y `calcular_costo()`.

También se utilizan parámetros opcionales en los métodos de cálculo de costos para permitir diferentes condiciones de impuesto y descuento.

## 7. Manejo de excepciones y validaciones

El sistema incorpora excepciones personalizadas para controlar situaciones relacionadas con clientes, servicios y reservas.

Se utilizan estructuras de manejo de errores:

- `try`
- `except`
- `else`
- `finally`

También se implementa el encadenamiento de excepciones mediante `raise ... from error`.

Las validaciones permiten rechazar información incorrecta, como tarifas no válidas, capacidades negativas o nulas, cantidades incorrectas, especialidades vacías y parámetros de cálculo fuera de los rangos permitidos.

## 8. Registro de eventos y errores

El sistema utiliza el módulo `logging` de Python para registrar eventos importantes y errores durante la ejecución.

Los registros se almacenan en el archivo `sistema.log`, lo que permite consultar el comportamiento del programa y revisar las situaciones inválidas detectadas.

## 9. Almacenamiento de información

El sistema no utiliza un motor de base de datos.

Los clientes, servicios y reservas se administran mediante listas en memoria durante la ejecución del programa. Esta estructura permite gestionar los objetos y realizar las operaciones solicitadas sin recurrir a una base de datos externa.

## 10. Requisitos de ejecución

Para ejecutar el proyecto se necesita:

- Tener Python 3 instalado.
- Contar con Visual Studio Code o una terminal compatible.
- Descargar o clonar el repositorio.
- Abrir la terminal en la carpeta principal del proyecto.

## 11. Ejecución del sistema

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

El programa ejecuta una simulación de las operaciones de registro de clientes, creación de servicios, gestión de reservas y control de situaciones inválidas.

## 12. Ejecución de pruebas

El proyecto incluye archivos de prueba para verificar el funcionamiento de los módulos.

Para ejecutar las pruebas, utilizar los siguientes comandos desde la carpeta principal:

**Pruebas generales**

```bash
python main.py
python prueba_logs.py
python prueba_reserva.py
```

**Pruebas de servicios**

```bash
python -m servicios.prueba_sala
python -m servicios.prueba_equipo
python -m servicios.prueba_asesoria
python -m servicios.prueba_validaciones_servicios
```

**Pruebas de reservas y excepciones**

```bash
python -m reservas.prueba_excepciones
python -m reservas.prueba_reserva
python -m reservas.prueba_reserva_invalida
python -m reservas.prueba_sin_cliente
python -m reservas.prueba_sin_servicio
python -m reservas.prueba_cancelacion
python -m reservas.prueba_procesamiento_pendiente
```

Estas pruebas permiten comprobar el registro de clientes, las validaciones de servicios, el cálculo de costos, la creación y procesamiento de reservas, las excepciones personalizadas y el control de operaciones no permitidas.

## 13. Repositorio del proyecto

El código fuente se encuentra disponible en el siguiente repositorio:

https://github.com/fernandopetro98-sys/Sistema-Integral-Software-FJ

## 14. Autoría y participación

Proyecto académico correspondiente a la Fase 4 del curso de Programación.

**Grupo:** 213023_629

**Integrantes:**

- Jose Fernando Petro Artuz.
- [Integrante 2].
- [Integrante 3].
- [Integrante 4].
- [Integrante 5].

La participación y los aportes de cada integrante deben corresponder a las actividades efectivamente desarrolladas y a las contribuciones registradas durante el trabajo colaborativo.

