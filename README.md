# Pasos para iniciar el proyecto

Este proyecto utiliza un entorno virtual de Python para gestionar sus dependencias. Sigue estos pasos para configurarlo correctamente.

---

## ✅ Requisitos previos
- Python 3.17.7 instalado.
- `pip` instalado.
- Clonar el proyecto
- Descargar la rama main2 (los cambios se encuentran aquí)
- Nota: Se subió el .env con la información, no necesita modificarse a menos que la clave de weather caduque.

---

## 🚀 Instrucciones de instalación

### 1. Crear un entorno virtual con `venv`
Ejecuta el siguiente comando en la terminal:
```bash
python3 -m venv venv
```

### 2. Una vez creado el entorno virtual, actívalo usando el siguiente comando en Mac:
```bash
source venv/bin/activate
```

### 3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```




## 🚀 Proceso de construcción del Front Weather y del Backend Weather API

Este proyecto ha sido construido utilizando varias herramientas de inteligencia artificial que me han ayudado a lo largo del desarrollo.

### 1. ChatGPT
ChatGPT fue una herramienta fundamental para el desarrollo del proyecto, ya que me permitió:

- Iniciar la API desde cero.
- Iniciar el front-end con Next.js desde cero.
- Proporcionar soluciones cuando me encontraba con errores, por ejemplo, al tener problemas con líneas de código o errores en la autenticación.

Algunas de las preguntas que le hice a ChatGPT fueron:

- "¿Puedes ayudarme con la siguiente línea de código?"
- "Estoy construyendo un front-end con autenticación en Next.js y tengo el siguiente error. La línea que causa problemas es esta…"

### 2. Copiloto Free
Copiloto Free me ayudó con el autocompletado de código en Visual Studio Code. Fue especialmente útil cuando tenía errores de sintaxis. Simplemente presionaba el botón "Solucionar con copiloto" y me proporcionaba una solución para lo que estaba mal.

### 3. Warp
Warp es una terminal con IA integrada que me ayudó a recordar comandos y ofreció autocompletado. Cuando tenía dudas sobre cómo usar un comando o cuál debía usar a continuación, podía hacer preguntas directamente en la terminal usando `#` seguido del comando o también hacer preguntas en el chat integrado de Warp.

---

## 📝 Experiencia durante el desarrollo

Durante el desarrollo, algunos de los momentos más destacados fueron:

- **Base del front-end:** Empecé programando la base del front-end, específicamente la pestaña de "cities". Después pedí ayuda para decidir los colores y estilos a aplicar.
  
- **Autenticación con Next.js:** Tuve algunas dudas sobre cómo implementar la autenticación en Next.js. Aunque la parte de registro fue complicada y quedó inconclusa, la implementación del login con usuario y contraseña predeterminados y el manejo de sesiones fue más sencillo con la ayuda de ChatGPT.
