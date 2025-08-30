<div align="center">

# 🐍 Herencia en Python - POO

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=plastic&logo=python&logoColor=white)](https://python.org)
[![POO](https://img.shields.io/badge/Paradigma-POO-green?style=plastic&logo=python&logoColor=white)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![Herencia](https://img.shields.io/badge/Concepto-Herencia-orange?style=plastic&logo=python&logoColor=white)](https://docs.python.org/3/tutorial/classes.html)
[![License](https://img.shields.io/badge/License-MIT-red?style=plastic&logo=github&logoColor=white)](LICENSE)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=3776AB&center=true&vCenter=true&width=600&lines=Programaci%C3%B3n+Orientada+a+Objetos;Herencia+en+Python+%F0%9F%90%8D;Reutilizaci%C3%B3n+de+C%C3%B3digo;Polimorfismo+y+Encapsulaci%C3%B3n" alt="Typing SVG"/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

## 📋 Tabla de Contenidos

- [🎯 Descripción](#-descripción)
- [🔗 Conceptos de Herencia](#-conceptos-de-herencia)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🚀 Ejemplos Prácticos](#-ejemplos-prácticos)
- [⚡ Ejecución Rápida](#-ejecución-rápida)
- [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [📚 Recursos Adicionales](#-recursos-adicionales)

---

## 🎯 Descripción

Este repositorio contiene ejemplos prácticos y ejercicios sobre **Herencia en Python**, uno de los pilares fundamentales de la Programación Orientada a Objetos (POO). Aquí encontrarás implementaciones que demuestran cómo las clases pueden heredar atributos y métodos de otras clases, promoviendo la reutilización de código y la organización jerárquica.

<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="100" height="100"/>

**"La herencia permite crear nuevas clases basadas en clases existentes"**

</div>

---

## 🔗 Conceptos de Herencia

<div align="center">

### 🌟 Pilares de la POO

<img src="https://img.shields.io/badge/Encapsulación-FF6B6B?style=for-the-badge&logo=python&logoColor=white" height="40"/>
<img src="https://img.shields.io/badge/Herencia-4ECDC4?style=for-the-badge&logo=python&logoColor=white" height="40"/>
<img src="https://img.shields.io/badge/Polimorfismo-45B7D1?style=for-the-badge&logo=python&logoColor=white" height="40"/>
<img src="https://img.shields.io/badge/Abstracción-96CEB4?style=for-the-badge&logo=python&logoColor=white" height="40"/>

</div>

### 🔹 Tipos de Herencia Implementados

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **🔸 Simple** | Una clase hereda de una sola clase padre | `Animal` → `Perro` |
| **🔸 Múltiple** | Una clase hereda de múltiples clases | `Volador + Nadador` → `Pato` |
| **🔸 Multinivel** | Cadena de herencia en varios niveles | `Vehiculo` → `Coche` → `Deportivo` |
| **🔸 Jerárquica** | Múltiples clases heredan de una clase base | `Animal` → `Perro, Gato, Ave` |

---

## 📁 Estructura del Proyecto

```
📂 Herencia/
├── 📜 README.md
├── 🐍 herencia_simple.py
├── 🐍 herencia_multiple.py
├── 🐍 herencia_multinivel.py
├── 🐍 herencia_jerarquica.py
├── 📂 ejemplos/
│   ├── 🐍 animales.py
│   ├── 🐍 vehiculos.py
│   ├── 🐍 empleados.py
│   └── 🐍 figuras_geometricas.py
├── 📂 ejercicios/
│   ├── 🐍 ejercicio_01.py
│   ├── 🐍 ejercicio_02.py
│   └── 🐍 ejercicio_03.py
└── 📂 tests/
    ├── 🧪 test_herencia.py
    └── 🧪 test_ejemplos.py
```

---

## 🚀 Ejemplos Prácticos

### 🔹 Herencia Simple

```python
# 👤 Clase Base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"

# 👨‍🎓 Clase Derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}"
```

### 🔸 Herencia Múltiple

```python
# 🦅 Clases Base
class Volador:
    def volar(self):
        return "Estoy volando! 🦅"

class Nadador:
    def nadar(self):
        return "Estoy nadando! 🏊‍♂️"

# 🦆 Clase que hereda de ambas
class Pato(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def presentarse(self):
        return f"Soy {self.nombre}, un pato"
```

### 🔹 Polimorfismo

```python
# 🎵 Método polimórfico
class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "🎸 Tocando guitarra!"

class Piano(Instrumento):
    def tocar(self):
        return "🎹 Tocando piano!"
```

---

## ⚡ Ejecución Rápida

### 🖥️ Prerrequisitos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![OS](https://img.shields.io/badge/OS-Windows%20|%20macOS%20|%20Linux-lightgrey?style=flat-square)

</div>

### 🚀 Ejecutar Ejemplos

```bash
# 📥 Clonar el repositorio
git clone https://github.com/Arkanabytes/POO-Python.git

# 📂 Navegar a la carpeta
cd POO-Python/Programacion/Herencia

# 🐍 Ejecutar ejemplos
python herencia_simple.py
python herencia_multiple.py
python ejemplos/animales.py

# 🧪 Ejecutar tests (opcional)
python -m pytest tests/
```

### 💻 Ejemplo de Salida

```
🐍 === HERENCIA EN PYTHON ===

👤 Creando persona: Juan (25 años)
👋 Juan dice: Hola, soy Juan

👨‍🎓 Creando estudiante: María (20 años) - Ingeniería
👋 María dice: Hola, soy María  
📚 María está estudiando Ingeniería

✅ Herencia funcionando correctamente!
```

---

## 🛠️ Tecnologías Utilizadas

<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="60" height="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" alt="VS Code" width="60" height="60"/>
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/git.svg" alt="Git" width="60" height="60" fill="#F05032"/>

</div>

- **🐍 Python 3.8+** - Lenguaje principal
- **🔧 VS Code** - Editor recomendado
- **📦 Git** - Control de versiones
- **🧪 pytest** - Testing framework (opcional)

---

## 📚 Recursos Adicionales

### 📖 Documentación y Tutoriales

- [📘 Python Official Docs - Classes](https://docs.python.org/3/tutorial/classes.html)
- [📗 Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [📙 GeeksforGeeks - Inheritance](https://www.geeksforgeeks.org/inheritance-in-python/)

### 🎯 Conceptos Relacionados

<div align="center">

[![Encapsulación](https://img.shields.io/badge/📦-Encapsulación-blue?style=flat-square)](../Encapsulacion/)
[![Polimorfismo](https://img.shields.io/badge/🔄-Polimorfismo-green?style=flat-square)](../Polimorfismo/)
[![Abstracción](https://img.shields.io/badge/🎭-Abstracción-purple?style=flat-square)](../Abstraccion/)
[![Clases](https://img.shields.io/badge/🏗️-Clases-orange?style=flat-square)](../Clases/)

</div>

---

<div align="center">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 💫 Conecta Conmigo

<p align="center">
  <a href="https://linkedin.com/in/tu-perfil" target="_blank">
    <img src="https://img.icons8.com/color/64/000000/linkedin.png" alt="LinkedIn" width="50" height="50" style="margin: 10px; border-radius: 50%; transition: transform 0.3s ease, box-shadow 0.3s ease; box-shadow: 0 4px 15px rgba(0,119,181,0.4);" onmouseover="this.style.transform='scale(1.2) rotate(5deg)'; this.style.boxShadow='0 8px 25px rgba(0,119,181,0.6)';" onmouseout="this.style.transform='scale(1) rotate(0deg)'; this.style.boxShadow='0 4px 15px rgba(0,119,181,0.4)';"/>
  </a>
  <a href="https://tu-sitio-web.com" target="_blank">
    <img src="https://img.icons8.com/color/64/000000/domain.png" alt="Website" width="50" height="50" style="margin: 10px; border-radius: 50%; transition: transform 0.3s ease, box-shadow 0.3s ease; box-shadow: 0 4px 15px rgba(255,107,53,0.4);" onmouseover="this.style.transform='scale(1.2) rotate(-5deg)'; this.style.boxShadow='0 8px 25px rgba(255,107,53,0.6)';" onmouseout="this.style.transform='scale(1) rotate(0deg)'; this.style.boxShadow='0 4px 15px rgba(255,107,53,0.4)';"/>
  </a>
  <a href="https://wa.me/tu-numero" target="_blank">
    <img src="https://img.icons8.com/color/64/000000/whatsapp.png" alt="WhatsApp" width="50" height="50" style="margin: 10px; border-radius: 50%; transition: transform 0.3s ease, box-shadow 0.3s ease; box-shadow: 0 4px 15px rgba(37,211,102,0.4);" onmouseover="this.style.transform='scale(1.2) rotate(5deg)'; this.style.boxShadow='0 8px 25px rgba(37,211,102,0.6)';" onmouseout="this.style.transform='scale(1) rotate(0deg)'; this.style.boxShadow='0 4px 15px rgba(37,211,102,0.4)';"/>
  </a>
  <a href="mailto:tu-email@ejemplo.com" target="_blank">
    <img src="https://img.icons8.com/color/64/000000/gmail.png" alt="Email" width="50" height="50" style="margin: 10px; border-radius: 50%; transition: transform 0.3s ease, box-shadow 0.3s ease; box-shadow: 0 4px 15px rgba(209,72,54,0.4);" onmouseover="this.style.transform='scale(1.2) rotate(-5deg)'; this.style.boxShadow='0 8px 25px rgba(209,72,54,0.6)';" onmouseout="this.style.transform='scale(1) rotate(0deg)'; this.style.boxShadow='0 4px 15px rgba(209,72,54,0.4)';"/>
  </a>
  <a href="https://github.com/Arkanabytes" target="_blank">
    <img src="https://img.icons8.com/color/64/000000/github--v1.png" alt="GitHub" width="50" height="50" style="margin: 10px; border-radius: 50%; transition: transform 0.3s ease, box-shadow 0.3s ease; box-shadow: 0 4px 15px rgba(36,41,46,0.4);" onmouseover="this.style.transform='scale(1.2) rotate(5deg)'; this.style.boxShadow='0 8px 25px rgba(36,41,46,0.6)';" onmouseout="this.style.transform='scale(1) rotate(0deg)'; this.style.boxShadow='0 4px 15px rgba(36,41,46,0.4)';"/>
  </a>
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

### 🌟 *"La herencia es la clave para construir software reutilizable y mantenible"* 🌟

<img src="https://img.shields.io/badge/Made%20with-❤️%20&%20Python-red?style=for-the-badge&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/Open%20Source-💚-green?style=for-the-badge&logoColor=white" height="30"/>

**¡Gracias por explorar la herencia en Python! 🐍✨**

</div>
