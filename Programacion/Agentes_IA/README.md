# 🤖 Agentes de IA - Programación Orientada a Objetos

Un proyecto que implementa agentes de inteligencia artificial utilizando los principios de la Programación Orientada a Objetos (POO) en Python.

## 📋 Descripción

Este proyecto forma parte del repositorio **POO-Python** y se centra en la implementación de agentes de inteligencia artificial utilizando conceptos avanzados de programación orientada a objetos. Los agentes pueden realizar tareas automatizadas, tomar decisiones y interactuar con su entorno de manera inteligente.

## 🚀 Características

- ✨ **Arquitectura basada en POO**: Implementación modular y escalable
- 🧠 **Agentes inteligentes**: Capacidad de toma de decisiones autónomas
- 🔄 **Gestión de memoria**: Manejo eficiente del historial y contexto
- 🛠️ **Integración de herramientas**: Soporte para múltiples APIs y servicios
- 🎯 **Casos de uso reales**: Ejemplos prácticos de implementación

## 📁 Estructura del Proyecto

```
Agentes_IA/
├── main.py              # Punto de entrada principal
├── agents/              # Clases de agentes
├── tools/               # Herramientas y utilidades
├── models/              # Modelos de datos
├── config/              # Configuraciones
└── examples/            # Ejemplos de uso
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **OpenAI API** (opcional)
- **LangChain** (opcional)
- **Requests** para llamadas HTTP
- **JSON** para manejo de datos

## 📦 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Arkanabytes/POO-Python.git
   cd POO-Python/Programacion/Agentes_IA/
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno** (si es necesario):
   ```bash
   cp .env.example .env
   # Edita .env con tus claves API
   ```

## 🎮 Uso

### Ejecución básica

```bash
python main.py
```

### Ejemplo de código

```python
from agents import IntelligentAgent
from tools import WebSearchTool, CalculatorTool

# Crear un agente
agent = IntelligentAgent(
    name="Asistente Virtual",
    description="Un agente capaz de buscar información y realizar cálculos"
)

# Agregar herramientas
agent.add_tool(WebSearchTool())
agent.add_tool(CalculatorTool())

# Ejecutar una tarea
result = agent.execute("Busca información sobre Python y calcula 25 * 4")
print(result)
```

## 🏗️ Arquitectura

### Clases Principales

- **`Agent`**: Clase base para todos los agentes
- **`IntelligentAgent`**: Agente con capacidades de IA
- **`Tool`**: Clase base para herramientas
- **`Memory`**: Gestión de memoria y contexto
- **`Environment`**: Entorno de ejecución

### Principios de POO Aplicados

- **Encapsulación**: Cada agente mantiene su estado interno
- **Herencia**: Jerarquía de clases de agentes especializados
- **Polimorfismo**: Interfaz común para diferentes tipos de agentes
- **Abstracción**: Separación entre implementación y uso

## 📚 Conceptos Implementados

### Agentes de IA
Los agentes implementados siguen el patrón:
1. **Percepción**: Reciben información del entorno
2. **Procesamiento**: Analizan y toman decisiones
3. **Acción**: Ejecutan tareas basadas en sus decisiones

### Gestión de Memoria
- Memoria a corto plazo para contexto inmediato
- Memoria a largo plazo para aprendizaje persistente
- Sistema de olvido para optimizar recursos

## 🎯 Casos de Uso

- **Asistente Virtual**: Responde preguntas y realiza tareas
- **Automatización de Procesos**: Ejecuta workflows complejos
- **Análisis de Datos**: Procesa y analiza información
- **Chatbots Inteligentes**: Conversaciones naturales

## 🧪 Ejemplos

Consulta la carpeta `examples/` para ver implementaciones específicas:

- `basic_agent.py` - Agente básico
- `web_scraping_agent.py` - Agente para web scraping
- `data_analysis_agent.py` - Agente para análisis de datos

## 🤝 Contribución

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Variables de entorno configuradas (para APIs externas)

## 🐛 Problemas Conocidos

- Consulta la sección [Issues](https://github.com/Arkanabytes/POO-Python/issues) del repositorio
- Para reportar bugs, usa el template de issues

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Arkanabytes** - *Desarrollo inicial* - [@Arkanabytes](https://github.com/Arkanabytes)

## 🙏 Agradecimientos

- Inspirado en los conceptos de IA y agentes inteligentes
- Gracias a la comunidad de Python y IA
- Recursos de aprendizaje de POO aplicada a IA

## 📞 Contacto

¿Tienes preguntas o sugerencias? Abre un issue en el repositorio o contacta al autor.

---

⭐ **¡Dale una estrella al repositorio si te resultó útil!** ⭐
