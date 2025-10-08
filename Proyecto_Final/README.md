```mermaid
classDiagram
    class Usuario {
        <<abstract>>
        - nombre: str
        - rut: str
        - email: str
        - telefono: str
        + __init__(nombre, rut, email, telefono)
        + mostrar_info()* void
        + get_nombre() str
        + get_rut() str
    }
    
    class Estudiante {
        - carrera: str
        - año: int
        - saldo_cuenta: float
        - asignaturas: List~Asignatura~
        + __init__(nombre, rut, email, telefono, carrera, año, saldo_cuenta)
        + pagar_servicio(monto: float) bool
        + inscribir_asignatura(asignatura: Asignatura) void
        + mostrar_info() void
        + agregar_saldo(monto: float) void
        + get_saldo() float
        + get_asignaturas() List~Asignatura~
    }
    
    class Conductor {
        - patente: str
        - tipo_vehiculo: str
        - calificacion: float
        - viajes_realizados: int
        + __init__(nombre, rut, email, telefono, patente, tipo_vehiculo)
        + calcular_tarifa(distancia_km: float) float
        + registrar_viaje(distancia_km: float, estudiante: Estudiante) bool
        + mostrar_info() void
        + get_calificacion() float
    }
    
    class Producto {
        - nombre: str
        - precio: float
        - categoria: str
        + __init__(nombre, precio, categoria)
        + get_nombre() str
        + get_precio() float
        + get_categoria() str
        + to_dict() dict
    }
    
    class Pedido {
        - id_pedido: int
        - productos: List~Producto~
        - precio_total: float
        - estado: str
        - estudiante: Estudiante
        - fecha: datetime
        + __init__(id_pedido, estudiante)
        + agregar_producto(producto: Producto) void
        + calcular_total() float
        + confirmar() bool
        + cambiar_estado(nuevo_estado: str) void
        + get_estado() str
        + get_productos() List~Producto~
    }
    
    class Asignatura {
        - codigo: str
        - nombre: str
        - profesor: str
        - creditos: int
        + __init__(codigo, nombre, profesor, creditos)
        + get_nombre() str
        + get_profesor() str
        + get_creditos() int
        + get_codigo() str
    }
    
    class Horario {
        - dia: str
        - hora_inicio: str
        - hora_fin: str
        - asignaturas: List~Asignatura~
        + __init__(dia, hora_inicio, hora_fin)
        + agregar_asignatura(asignatura: Asignatura) void
        + verificar_choque(otro_horario: Horario) bool
        + get_asignaturas() List~Asignatura~
        + mostrar_horario() void
    }
    
    Usuario <|-- Estudiante
    Usuario <|-- Conductor
    Estudiante "1" --> "*" Pedido: realiza
    Pedido "1" --> "*" Producto: contiene
    Estudiante "1" --> "*" Asignatura: inscribe
    Horario "1" --> "*" Asignatura: incluye
    Conductor "1" --> "*" Estudiante: transporta
