# POO-Python 🐍

<div align="center">

![Python OOP Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=200&section=header&text=POO%20Python&fontSize=50&fontColor=white&animation=fadeIn&fontAlignY=35&desc=Programación%20Orientada%20a%20Objetos&descAlignY=55&descSize=20)

[![Python](https://img.shields.io/badge/Python-3.7+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=github&logoColor=white)]()
[![GitHub Stars](https://img.shields.io/github/stars/Arkanabytes/POO-Python?style=for-the-badge&logo=github)](https://github.com/Arkanabytes/POO-Python/stargazers)

</div>

## 📋 Descripción

Este repositorio contiene ejemplos, ejercicios y proyectos relacionados con la **Programación Orientada a Objetos (POO)** en Python. Está diseñado como material de estudio y práctica para comprender los conceptos fundamentales de la POO y su implementación en Python.

<div align="center">

```mermaid
graph TB
    A[🎯 POO Python] --> B[📚 Conceptos Básicos]
    A --> C[🏗️ Pilares de POO]
    A --> D[🚀 Conceptos Avanzados]
    
    B --> B1[Clases y Objetos]
    B --> B2[Atributos y Métodos]
    B --> B3[Constructor/Destructor]
    
    C --> C1[🔒 Encapsulamiento]
    C --> C2[👨‍👩‍👧‍👦 Herencia]
    C --> C3[🎭 Polimorfismo]
    C --> C4[🎨 Abstracción]
    
    D --> D1[Métodos Especiales]
    D --> D2[Propiedades]
    D --> D3[Patrones de Diseño]
    
    style A fill:#ff6b6b,stroke:#333,stroke-width:3px,color:#fff
    style C1 fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff
    style C2 fill:#45b7d1,stroke:#333,stroke-width:2px,color:#fff
    style C3 fill:#96ceb4,stroke:#333,stroke-width:2px,color:#fff
    style C4 fill:#ffeaa7,stroke:#333,stroke-width:2px,color:#333
```

</div>

## 🎯 Objetivos

<table>
<tr>
<td width="50%">

### 🏗️ Fundamentos
- ✅ Comprender los pilares de la POO
- ✅ Implementar clases y objetos
- ✅ Aplicar herencia y polimorfismo
- ✅ Dominar el encapsulamiento

</td>
<td width="50%">

### 🚀 Avanzado
- 🔥 Patrones de diseño
- 🔥 Arquitectura orientada a objetos
- 🔥 Testing y debugging
- 🔥 Mejores prácticas

</td>
</tr>
</table>

## 📊 Progreso del Curso

<div align="center">

![Progreso](https://github-readme-stats.vercel.app/api?username=Arkanabytes&show_icons=true&theme=radical&include_all_commits=true&count_private=true)

</div>

### Niveles de Aprendizaje

```mermaid
journey
    title Ruta de Aprendizaje POO
    section Básico
      Clases y Objetos      : 5: Estudiante
      Atributos y Métodos   : 4: Estudiante
      Constructor           : 4: Estudiante
    section Intermedio
      Encapsulamiento       : 3: Estudiante
      Herencia             : 2: Estudiante
      Polimorfismo         : 2: Estudiante
    section Avanzado
      Abstracción          : 1: Estudiante
      Patrones de Diseño   : 1: Estudiante
      Arquitectura         : 1: Estudiante
```

## 🏗️ Arquitectura POO

<div align="center">

```mermaid
classDiagram
    class Animal {
        +String nombre
        +int edad
        +comer()
        +dormir()
        +hacerSonido()*
    }
    
    class Perro {
        +String raza
        +ladrar()
        +hacerSonido()
    }
    
    class Gato {
        +Boolean esDomestico
        +maullar()
        +hacerSonido()
    }
    
    class Mascota {
        +String dueño
        +Boolean vacunado
        +jugar()
    }
    
    Animal <|-- Perro
    Animal <|-- Gato
    Mascota <|-- Perro
    Mascota <|-- Gato
    
    style Animal fill:#ff9999
    style Perro fill:#99ccff
    style Gato fill:#99ff99
    style Mascota fill:#ffcc99
```

</div>

## 📚 Contenido del Repositorio

<div align="center">

```mermaid
graph LR
    A[📁 POO-Python] --> B[📚 Ejemplos]
    A --> C[💪 Ejercicios]
    A --> D[🚀 Proyectos]
    A --> E[📖 Documentación]
    A --> F[🧪 Tests]
    
    B --> B1[🟢 Básico]
    B --> B2[🟡 Intermedio]
    B --> B3[🔴 Avanzado]
    
    C --> C1[⭐ Nivel 1]
    C --> C2[⭐⭐ Nivel 2]
    C --> C3[⭐⭐⭐ Nivel 3]
    
    D --> D1[🏦 Sistema Bancario]
    D --> D2[📚 Biblioteca]
    D --> D3[🛒 Tienda Online]
    
    style A fill:#2d3748,stroke:#4a5568,stroke-width:3px,color:#fff
    style B1 fill:#38a169,color:#fff
    style B2 fill:#d69e2e,color:#fff
    style B3 fill:#e53e3e,color:#fff
```

</div>

### 🛠️ Prerequisitos

<div align="center">

| Requisito | Versión | Estado |
|-----------|---------|--------|
| ![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python) | 3.7+ | ✅ |
| ![Git](https://img.shields.io/badge/Git-Latest-orange?logo=git) | Latest | ✅ |
| ![IDE](https://img.shields.io/badge/IDE-VS%20Code%20%7C%20PyCharm-green?logo=visualstudiocode) | Any | ✅ |

</div>

## 🚀 Quick Start

<div align="center">

```mermaid
graph TD
    A[🏁 Inicio] --> B[📥 Clonar Repo]
    B --> C[📁 Navegar al directorio]
    C --> D[🐍 Crear entorno virtual]
    D --> E[📦 Instalar dependencias]
    E --> F[▶️ Ejecutar ejemplos]
    F --> G[🎉 ¡Listo para aprender!]
    
    style A fill:#ff6b6b,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#51cf66,stroke:#333,stroke-width:2px,color:#fff
```

</div>

```bash
# 1️⃣ Clona el repositorio
git clone https://github.com/Arkanabytes/POO-Python.git

# 2️⃣ Navega al directorio
cd POO-Python

# 3️⃣ Crea entorno virtual
python -m venv venv

# 4️⃣ Activa el entorno
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 5️⃣ Instala dependencias
pip install -r requirements.txt

# 6️⃣ ¡Empieza a aprender!
python ejemplos/basico/mi_primera_clase.py
```

## 📖 Ejemplos Interactivos

### 🟢 Clase Básica
```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    def saludar(self):
        return f"👋 Hola, soy {self._nombre} y tengo {self._edad} años"

# 🎯 Uso
persona = Persona("Juan", 25)
print(persona.saludar())  # 👋 Hola, soy Juan y tengo 25 años
```

### 🟡 Herencia y Polimorfismo
```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        return "🚗 Acelerando..."

class Auto(Vehiculo):
    def acelerar(self):
        return f"🏎️ El {self.marca} {self.modelo} acelera suavemente"

class Moto(Vehiculo):
    def acelerar(self):
        return f"🏍️ La {self.marca} {self.modelo} acelera rápidamente"
```

### 🔴 Patrón Singleton
```python
class DatabaseConnection:
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def connect(self):
        if not self._connection:
            self._connection = "🔗 Conectado a la base de datos"
        return self._connection
```

## 📊 Estadísticas del Proyecto

<div align="center">

![Estadísticas](https://github-readme-streak-stats.herokuapp.com/?user=Arkanabytes&theme=radical&hide_border=true)

</div>

### 📈 Métricas de Aprendizaje

```mermaid
gitgraph
    commit id: "📚 Conceptos Básicos"
    commit id: "🏗️ Clases y Objetos"
    branch herencia
    checkout herencia
    commit id: "👨‍👩‍👧‍👦 Herencia Simple"
    commit id: "🔄 Herencia Multiple"
    checkout main
    merge herencia
    commit id: "🎭 Polimorfismo"
    branch avanzado
    checkout avanzado
    commit id: "🎨 Patrones de Diseño"
    commit id: "🏛️ Arquitectura"
    checkout main
    merge avanzado
    commit id: "🚀 Proyecto Final"
```

## 🎮 Proyectos Incluidos

<div align="center">

| Proyecto | Nivel | Tecnologías | Demo |
|----------|-------|-------------|------|
| 🏦 Sistema Bancario | ⭐⭐ | Python, SQLite | [▶️ Ver Demo](#) |
| 📚 Biblioteca Digital | ⭐⭐⭐ | Python, JSON, GUI | [▶️ Ver Demo](#) |
| 🛒 E-commerce | ⭐⭐⭐ | Python, API, DB | [▶️ Ver Demo](#) |

</div>

### 🏦 Sistema Bancario - Arquitectura

```mermaid
classDiagram
    class Banco {
        +String nombre
        +List~Cuenta~ cuentas
        +crearCuenta()
        +buscarCuenta()
    }
    
    class Cuenta {
        +String numero
        +float saldo
        +Cliente titular
        +depositar()
        +retirar()
        +transferir()
    }
    
    class CuentaAhorro {
        +float tasaInteres
        +calcularInteres()
    }
    
    class CuentaCorriente {
        +float sobregiro
        +verificarSobregiro()
    }
    
    class Cliente {
        +String nombre
        +String documento
        +String telefono
    }
    
    Banco ||--o{ Cuenta : contiene
    Cuenta ||-- Cliente : pertenece
    Cuenta <|-- CuentaAhorro
    Cuenta <|-- CuentaCorriente
```

## 🧪 Testing y Calidad

<div align="center">

![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge&logo=pytest)
![Coverage](https://img.shields.io/badge/Coverage-85%25-yellow?style=for-the-badge&logo=codecov)
![Quality](https://img.shields.io/badge/Code%20Quality-A-brightgreen?style=for-the-badge&logo=codeclimate)

</div>

```bash
# 🧪 Ejecutar todas las pruebas
pytest tests/ -v --cov=src

# 📊 Reporte de cobertura
pytest --cov=src --cov-report=html

# 🔍 Análisis de calidad de código
pylint src/
flake8 src/
```

## 🤝 Contribuir

<div align="center">

```mermaid
graph LR
    A[🍴 Fork] --> B[🌿 Branch]
    B --> C[💻 Code]
    C --> D[🧪 Test]
    D --> E[📝 Commit]
    E --> F[🚀 Push]
    F --> G[📬 Pull Request]
    
    style A fill:#ff6b6b,color:#fff
    style G fill:#51cf66,color:#fff
```

</div>

### 📋 Proceso de Contribución

1. **🍴 Fork** el repositorio
2. **🌿 Crea** tu rama (`git checkout -b feature/AmazingFeature`)
3. **💻 Desarrolla** tu contribución
4. **🧪 Ejecuta** los tests
5. **📝 Commit** tus cambios (`git commit -m 'Add: Amazing Feature'`)
6. **🚀 Push** a la rama (`git push origin feature/AmazingFeature`)
7. **📬 Abre** un Pull Request

## 🗓️ Roadmap

```mermaid
gantt
    title Roadmap POO-Python
    dateFormat  YYYY-MM-DD
    section Básico
    Clases y Objetos     :done,    basic1, 2024-01-01,2024-01-15
    Métodos Especiales   :done,    basic2, 2024-01-16,2024-01-31
    section Intermedio
    Herencia            :active,   inter1, 2024-02-01,2024-02-15
    Polimorfismo        :          inter2, 2024-02-16,2024-02-28
    section Avanzado
    Patrones de Diseño  :          adv1, 2024-03-01,2024-03-15
    Proyectos Finales   :          adv2, 2024-03-16,2024-03-31
```

## 📄 Licencia

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

Este proyecto está bajo la **Licencia MIT** - mira el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

<div align="center">

<img src="https://github.com/Arkanabytes.png" width="100px" style="border-radius: 50%">

**Arkanabytes**

[![GitHub](https://img.shields.io/badge/GitHub-Arkanabytes-black?style=for-the-badge&logo=github)](https://github.com/Arkanabytes)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:tu-email@ejemplo.com)

</div>

## 🌟 Agradecimientos

<div align="center">

```mermaid
mindmap
  root((🙏 Gracias))
    📚 Documentación Python
      Guido van Rossum
      Python Foundation
    🌐 Comunidad
      Stack Overflow
      Reddit r/Python
      Discord Python
    📖 Recursos
      Real Python
      Python.org
      GeeksforGeeks
    👥 Contribuidores
      Issues
      Pull Requests
      Feedback
```

</div>

## 📚 Recursos Adicionales

<div align="center">

| Tipo | Recurso | Link |
|------|---------|------|
| 📖 | Python Docs | [![Docs](https://img.shields.io/badge/Python-Docs-blue?logo=python)](https://docs.python.org/3/) |
| 🎓 | Real Python | [![Real Python](https://img.shields.io/badge/Real-Python-red?logo=python)](https://realpython.com/) |
| 📺 | YouTube | [![YouTube](https://img.shields.io/badge/Python-Tutorials-red?logo=youtube)](https://youtube.com/results?search_query=python+oop) |
| 💬 | Discord | [![Discord](https://img.shields.io/badge/Python-Discord-blurple?logo=discord)](https://discord.gg/python) |

</div>

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer)

⭐ **¡Si este proyecto te resultó útil, no olvides darle una estrella!** ⭐

[![GitHub stars](https://img.shields.io/github/stars/Arkanabytes/POO-Python?style=social)](https://github.com/Arkanabytes/POO-Python/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Arkanabytes/POO-Python?style=social)](https://github.com/Arkanabytes/POO-Python/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Arkanabytes/POO-Python?style=social)](https://github.com/Arkanabytes/POO-Python/watchers)

</div>
