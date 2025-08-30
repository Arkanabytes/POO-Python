<div align="center">

# 🎮 Cachipún - Piedra, Papel o Tijera 

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=plastic&logo=python&logoColor=white)](https://python.org)
[![Game](https://img.shields.io/badge/Juego-Cachip%C3%BAn-red?style=plastic&logo=gamepad&logoColor=white)](https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera)
[![POO](https://img.shields.io/badge/Paradigma-POO-green?style=plastic&logo=python&logoColor=white)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![Version](https://img.shields.io/badge/Versi%C3%B3n-1.0-orange?style=plastic&logo=github&logoColor=white)](https://github.com/Arkanabytes)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=FF6B6B&center=true&vCenter=true&multiline=true&width=700&height=80&lines=%F0%9F%AA%A8+%F0%9F%93%84+%E2%9C%82%EF%B8%8F+Cachip%C3%BAn+Cl%C3%A1sico;Programaci%C3%B3n+Orientada+a+Objetos;%C2%A1Div%C3%A9rtete+programando!+%F0%9F%8E%89" alt="Typing SVG"/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

## 🎯 Descripción del Juego

**Cachipún** (también conocido como Piedra, Papel o Tijera) es un juego clásico implementado en Python usando **Programación Orientada a Objetos**. Este proyecto demuestra conceptos fundamentales de POO como clases, objetos, métodos y encapsulación en un contexto divertido e interactivo.

<div align="center">

### 🎲 Reglas del Juego

| Jugada | Vence a | Pierde contra |
|--------|---------|---------------|
| 🪨 **Piedra** | ✂️ Tijera | 📄 Papel |
| 📄 **Papel** | 🪨 Piedra | ✂️ Tijera |
| ✂️ **Tijera** | 📄 Papel | 🪨 Piedra |

</div>

---

## 📋 Tabla de Contenidos

- [🚀 Características](#-características)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚡ Instalación y Ejecución](#-instalación-y-ejecución)
- [🎮 Cómo Jugar](#-cómo-jugar)
- [🏗️ Arquitectura POO](#️-arquitectura-poo)
- [📸 Screenshots](#-screenshots)
- [🛠️ Tecnologías](#️-tecnologías)
- [🔮 Futuras Mejoras](#-futuras-mejoras)

---

## 🚀 Características

<div align="center">

### ✨ Funcionalidades Principales

<img src="https://img.shields.io/badge/🎯-Juego_Clásico-FF6B6B?style=for-the-badge" height="35"/>
<img src="https://img.shields.io/badge/🤖-IA_Inteligente-4ECDC4?style=for-the-badge" height="35"/>
<img src="https://img.shields.io/badge/📊-Estadísticas-45B7D1?style=for-the-badge" height="35"/>
<img src="https://img.shields.io/badge/🎨-Interfaz_Colorida-96CEB4?style=for-the-badge" height="35"/>

</div>

- **🎮 Interfaz Interactiva**: Menús coloridos y fáciles de usar
- **🤖 Oponente IA**: Computadora con jugadas aleatorias inteligentes
- **📊 Sistema de Puntuación**: Lleva el registro de victorias, derrotas y empates
- **🎯 Validación de Jugadas**: Control de entradas del usuario
- **🔄 Juego Continuo**: Rondas múltiples hasta que decidas salir
- **🎨 Emojis y Colores**: Experiencia visual atractiva
- **📈 Estadísticas Detalladas**: Historial completo de partidas

---

## 📁 Estructura del Proyecto

```
📂 Juego_Cachipun/
├── 📜 README.md
├── 🐍 main.py                 # Archivo principal del juego
├── 🐍 cachipun.py             # Clase principal del juego
├── 🐍 jugador.py              # Clase Jugador
├── 🐍 computadora.py          # Clase Computadora (IA)
├── 🐍 estadisticas.py         # Clase para manejar stats
├── 📂 utils/
│   ├── 🐍 __init__.py
│   ├── 🐍 colores.py          # Colores para la terminal
│   ├── 🐍 validaciones.py     # Funciones de validación
│   └── 🐍 helpers.py          # Funciones auxiliares
├── 📂 tests/
│   ├── 🧪 test_cachipun.py
│   ├── 🧪 test_jugador.py
│   └── 🧪 test_validaciones.py
└── 📂 docs/
    ├── 📄 reglas.md
    └── 📄 arquitectura.md
```

---

## ⚡ Instalación y Ejecución

### 🖥️ Prerrequisitos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-Cualquiera-black?style=flat-square&logo=terminal&logoColor=white)
![OS](https://img.shields.io/badge/OS-Windows%20|%20macOS%20|%20Linux-lightgrey?style=flat-square)

</div>

### 🚀 Pasos para Ejecutar

```bash
# 📥 1. Clonar el repositorio
git clone https://github.com/Arkanabytes/POO-Python.git

# 📂 2. Navegar al directorio del juego
cd POO-Python/Programacion/Juego_Cachipun

# 🐍 3. Ejecutar el juego
python main.py

# 🎮 4. ¡A jugar! Sigue las instrucciones en pantalla
```

### 🔧 Instalación Alternativa

```bash
# 📦 Opción con virtual environment (recomendado)
python -m venv cachipun_env
source cachipun_env/bin/activate  # Linux/macOS
# cachipun_env\Scripts\activate    # Windows

pip install -r requirements.txt  # Si existe
python main.py
```

---

## 🎮 Cómo Jugar

### 🎯 Instrucciones Paso a Paso

1. **🚀 Inicia el juego** ejecutando `python main.py`
2. **✍️ Ingresa tu nombre** cuando se te solicite
3. **🎲 Elige tu jugada:**
   - `1` o `piedra` para 🪨 Piedra
   - `2` o `papel` para 📄 Papel  
   - `3` o `tijera` para ✂️ Tijera
4. **🤖 La computadora** hará su jugada automáticamente
5. **🏆 Ve el resultado** y las estadísticas actualizadas
6. **🔄 Continúa jugando** o sal del juego cuando quieras

### 💻 Ejemplo de Partida

```
🎮 =================== CACHIPÚN ===================

👤 Jugador: Arkanabytes
🤖 Computadora: Bot-Python

📊 ESTADÍSTICAS ACTUALES:
   🏆 Victorias: 2  |  💀 Derrotas: 1  |  🤝 Empates: 1

🎯 Elige tu jugada:
   1️⃣ 🪨 Piedra
   2️⃣ 📄 Papel  
   3️⃣ ✂️ Tijera
   ❌ 'salir' para terminar

➤ Tu elección: 1

🪨 Arkanabytes eligió: PIEDRA
✂️ Bot-Python eligió: TIJERA

🎉 ¡GANASTE! 🪨 Piedra vence a ✂️ Tijera

📈 ESTADÍSTICAS ACTUALIZADAS:
   🏆 Victorias: 3  |  💀 Derrotas: 1  |  🤝 Empates: 1
```

---

## 🏗️ Arquitectura POO

### 🔧 Clases Principales

<div align="center">

```mermaid
classDiagram
    class Cachipun {
        -jugador: Jugador
        -computadora: Computadora  
        -estadisticas: Estadisticas
        +iniciar_juego()
        +nueva_ronda()
        +determinar_ganador()
        +mostrar_resultado()
    }
    
    class Jugador {
        -nombre: str
        -jugada_actual: str
        +hacer_jugada()
        +obtener_nombre()
    }
    
    class Computadora {
        -nombre: str
        -dificultad: str
        +hacer_jugada_aleatoria()
        +jugada_inteligente()
    }
    
    class Estadisticas {
        -victorias: int
        -derrotas: int
        -empates: int
        +actualizar_stats()
        +mostrar_resumen()
        +resetear_stats()
    }
    
    Cachipun --> Jugador
    Cachipun --> Computadora
    Cachipun --> Estadisticas
```

</div>

### 🎯 Conceptos POO Implementados

| Concepto | Implementación | Ejemplo |
|----------|----------------|---------|
| **🏗️ Encapsulación** | Atributos privados y métodos públicos | `_nombre`, `obtener_nombre()` |
| **🔄 Herencia** | Clases especializadas | `JugadorHumano` ← `Jugador` |
| **🎭 Polimorfismo** | Métodos con mismo nombre, diferente comportamiento | `hacer_jugada()` |
| **🎨 Abstracción** | Ocultar complejidad interna | `determinar_ganador()` |

---

## 📸 Screenshots

<div align="center">

### 🏠 Pantalla de Inicio
```
🎮 ========================================
    🪨 📄 ✂️  CACHIPÚN PYTHON POO  ✂️ 📄 🪨
🎮 ========================================

👋 ¡Bienvenido al juego más clásico!
🎯 Demuestra tu suerte contra la computadora

✍️ Ingresa tu nombre: Arkanabytes
🤖 Tu oponente será: Bot-Python

🚀 ¡Comenzemos a jugar!
```

### 🎲 Durante el Juego
```
🎯 RONDA #5

🪨 Arkanabytes: PIEDRA    vs    📄 Bot-Python: PAPEL

😅 ¡Perdiste! 📄 Papel envuelve a 🪨 Piedra

📊 Score: 🏆 2  💀 2  🤝 1
```

### 🏆 Final del Juego
```
🎊 =============== RESUMEN FINAL ===============

👤 Jugador: Arkanabytes
🎮 Partidas jugadas: 10

📈 ESTADÍSTICAS FINALES:
   🏆 Victorias: 4 (40%)
   💀 Derrotas: 3 (30%)
   🤝 Empates: 3 (30%)

🎯 Tu jugada favorita: 🪨 Piedra (5 veces)
🤖 La computadora prefirió: ✂️ Tijera (4 veces)

🌟 ¡Gracias por jugar! ¡Vuelve pronto!
```

</div>

---

## 🛠️ Tecnologías

<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="80" height="80"/>
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/git.svg" alt="Git" width="80" height="80" fill="#F05032"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" alt="VS Code" width="80" height="80"/>

</div>

### 📦 Stack Tecnológico

- **🐍 Python 3.8+** - Lenguaje principal
- **🎨 Colorama** - Colores en terminal (opcional)
- **🧪 pytest** - Testing framework
- **📊 Random** - Generación de jugadas aleatorias
- **⏰ Time** - Delays y animaciones
- **🔧 OS** - Limpieza de terminal multiplataforma

---

## 🔮 Futuras Mejoras

### 🚀 Roadmap v2.0

<div align="center">

[![Mejora](https://img.shields.io/badge/🎮-Interfaz_Gráfica-blue?style=for-the-badge)](https://tkinter.org)
[![Mejora](https://img.shields.io/badge/🌐-Multijugador_Online-green?style=for-the-badge)](https://socket.io)
[![Mejora](https://img.shields.io/badge/🤖-IA_Avanzada-red?style=for-the-badge)](https://scikit-learn.org)
[![Mejora](https://img.shields.io/badge/💾-Base_de_Datos-yellow?style=for-the-badge)](https://sqlite.org)

</div>

- **🎨 GUI con Tkinter**: Interfaz gráfica moderna
- **🧠 IA Inteligente**: Algoritmos de machine learning
- **🌐 Modo Online**: Jugar contra otros jugadores
- **💾 Persistencia**: Guardar estadísticas en base de datos
- **🏆 Sistema de Rangos**: Niveles y achievements
- **🎵 Efectos de Sonido**: Audio feedback
- **📱 Versión Mobile**: App para Android/iOS
- **🎮 Torneos**: Competencias entre jugadores

### 🔧 Posibles Extensiones

```python
# 🎯 Variantes del juego
class CachipunExtendido(Cachipun):
    """Versión con Lagarto y Spock"""
    jugadas = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']

# 🤖 IA con aprendizaje
class IAInteligente(Computadora):
    """IA que aprende de patrones del jugador"""
    def __init__(self):
        self.historial_jugador = []
        self.predictor = MLPredictor()
```

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

### 🎮 *"Un juego simple, pero con gran arquitectura de código"* 🎮

<img src="https://img.shields.io/badge/Made%20with-❤️%20&%20Python-red?style=for-the-badge&logoColor=white" height="30"/>
<img src="https://img.shields.io/badge/Juego-Divertido%20%F0%9F%8E%89-orange?style=for-the-badge&logoColor=white" height="30"/>

**¡Que gane el mejor! 🪨📄✂️**

</div>
