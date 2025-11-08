# Retro Super Snake - Juego en Python con POO

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![Game Screenshot](https://github.com/lozadandres/Juego-Retro-Super-Snake-con-POO-en-Python---Univalle-Tulu-/assets/172821184/8c91a017-07e7-4b06-80ed-949593fe2820)

## 📋 Descripción

**Retro Super Snake** es una implementación moderna y educativa del clásico juego de la serpiente, desarrollado en Python utilizando el paradigma de Programación Orientada a Objetos (POO). Este proyecto demuestra el uso efectivo de conceptos avanzados como herencia, polimorfismo, encapsulamiento y composición, mientras ofrece una experiencia de juego atractiva con mecánicas adicionales que van más allá del juego tradicional.

El proyecto fue desarrollado como parte del currículo académico de la Universidad del Valle - Sede Tuluá, sirviendo como ejemplo práctico de cómo aplicar principios de POO en el desarrollo de videojuegos.

## 🎮 Características Principales

- **🐍 Serpiente Dinámica**: Movimiento fluido con crecimiento progresivo
- **🍎 Sistema de Alimentos**: Manzanas rojas que otorgan puntos y crecimiento
- **🚧 Obstáculos**: Elementos fijos que aumentan la dificultad
- **⭐ Items Especiales**:
  - **Speed Boost**: Aumenta temporalmente la velocidad de la serpiente
  - **Score Boost**: Otorga puntos extra
- **⏸️ Pausa del Juego**: Funcionalidad para pausar y reanudar
- **🎨 Gráficos Retro**: Estilo visual nostálgico con sprites personalizados
- **📊 Sistema de Puntuación**: Seguimiento de puntuación en tiempo real
- **🎯 Pantallas Interactivas**: Menú de inicio y pantalla de Game Over

## 🏗️ Arquitectura del Proyecto

El proyecto está estructurado siguiendo los principios SOLID y utiliza un diseño modular:

```
Juego Retro Super Snake con POO en Python/
├── main.py                 # Punto de entrada del juego
├── game.py                 # Clase principal Game (controlador)
├── snake.py                # Clase Snake (modelo principal)
├── food.py                 # Clase Food (elemento consumible)
├── obstacle.py             # Clase Obstacle (elemento estático)
├── special_item.py         # Clase SpecialItem (power-ups)
├── game_object.py          # Clase base GameObject
├── utils.py                # Constantes y utilidades
└── assets/
    └── imagenes/           # Sprites y recursos gráficos
```

### Diagrama UML de Clases

![Diagrama UML](https://github.com/lozadandres/Juego-Retro-Super-Snake-con-POO-en-Python---Univalle-Tulu-/assets/172821184/da1f5d12-91f7-4943-b117-d5698c333772)

## 🚀 Instalación y Ejecución

### Prerrequisitos

- **Python 3.8 o superior**
- **Pygame 2.0+**

### Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/lozadandres/Juego-Retro-Super-Snake-con-POO-en-Python---Univalle-Tulua.git
   cd Juego-Retro-Super-Snake-con-POO-en-Python---Univalle-Tulua
   ```

2. **Instala las dependencias:**
   ```bash
   pip install pygame
   ```

3. **Ejecuta el juego:**
   ```bash
   python "Juego Retro Super Snake con POO en Python/main.py"
   ```

## 🎮 Controles

| Tecla | Acción |
|-------|--------|
| `W` | Mover arriba |
| `A` | Mover izquierda |
| `S` | Mover abajo |
| `D` | Mover derecha |
| `Espacio` | Pausar/Reanudar |
| Cualquier tecla | Iniciar juego / Reiniciar |

## 🎯 Mecánicas de Juego

### Objetivo
Guía a la serpiente para consumir la mayor cantidad posible de manzanas mientras evitas colisionar con:
- Las paredes del escenario
- El propio cuerpo de la serpiente
- Obstáculos fijos en el mapa

### Sistema de Puntuación
- **Manzana normal**: +10 puntos
- **Item especial de puntuación**: +50 puntos
- **Aumento de velocidad**: La velocidad del juego aumenta gradualmente con la puntuación

### Items Especiales
- Aparecen aleatoriamente después de consumir manzanas
- **Speed Boost**: Aumenta temporalmente la velocidad de movimiento
- **Score Boost**: Otorga puntos extra instantáneos

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación principal
- **Pygame**: Framework para desarrollo de videojuegos
- **Programación Orientada a Objetos**: Paradigma de diseño implementado
- **Sprites Personalizados**: Recursos gráficos creados para el proyecto

## 📚 Conceptos de POO Implementados

- **Herencia**: `GameObject` como clase base para elementos del juego
- **Polimorfismo**: Métodos `draw()` y `update()` en diferentes clases
- **Encapsulamiento**: Atributos privados y métodos de acceso
- **Composición**: Relaciones entre objetos del juego
- **Abstracción**: Interfaces comunes para diferentes tipos de objetos

## 🎥 Demo

[![Video Demo](https://img.youtube.com/vi/J3YhwaTR3kg/0.jpg)](https://youtu.be/J3YhwaTR3kg)

*Haz clic en la imagen para ver el video de demostración*

## 👥 Contribuidores

- **Andrés Lozada** - Desarrollador principal
- **Universidad del Valle - Sede Tuluá** - Institución académica

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Inspirado en el clásico juego Snake
- Desarrollado como proyecto académico para demostrar conceptos de POO
- Recursos gráficos obtenidos de fuentes libres y creados para el proyecto

---

**¡Disfruta jugando Retro Super Snake y explora el poder de la Programación Orientada a Objetos!** 🐍✨
