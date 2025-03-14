# 🖥️ Prueba Técnica - Ingeniero de Aplicaciones Full Stack 🚀

## 📌 Introducción

¡Hola, equipo de **Emtelco**! 👋
¡Link del proyecto desplegado: **[http://143.198.153.239/](http://143.198.153.239/)** 🌎

Soy **Carlos Andres Loaiza Ruiz**, y comparto mi prueba técnica para el cargo de **Ingeniero de Aplicaciones Full Stack**. 🚀

Este proyecto implementa una **API REST** con **Django REST Framework** para la gestión de vulnerabilidades NIST en una infraestructura en la nube. Se desarrollaron los endpoints requeridos, incluyendo un extra para eliminar vulnerabilidades. Además, se incorporaron funcionalidades adicionales como **autenticación con tokens, auditoría de logs, tests automáticos** y **despliegue en la nube con Digital Ocean**.

---

## 📦 Instalación y Ejecución con Docker

### 1️⃣ **Clonar el repositorio**
```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
```

### 2️⃣ **Configurar variables de entorno**
Renombra el archivo **`.env.example`** a **`.env`** y ajusta las variables necesarias:
```bash
   cp .env.example .env
```

### 3️⃣ **Levantar los servicios con Docker** 🚀
```bash
   docker-compose up --build -d
```
Esto descargará las imágenes necesarias y pondrá en marcha la API junto con MySQL.

### 4️⃣ **Verificar contenedores en ejecución**
```bash
   docker ps
```
Deberías ver los contenedores de la API y la base de datos corriendo.

---

## 🗄️ **Tecnologías utilizadas**

- **Python 3.x** 🐍
- **Django REST Framework** 🛠️
- **MySQL** 🗄️
- **Docker & Docker Compose** 🐳
- **Digital Ocean (Despliegue en la nube)** ☁️
- **Autenticación con Token** 🔑
- **Logging & Auditoría** 📄
- **Pytest (Pruebas Unitarias)** 🧪

---

## 🚀 **Endpoints de la API**

### 1️⃣ **Listado de vulnerabilidades** 📋
- **URL:** `/api/vulnerabilities/`
- **Método:** `GET`
- **Descripción:** Devuelve el listado total de vulnerabilidades.

### 2️⃣ **Registrar vulnerabilidades fijas** ✅
- **URL DESPLEGADA:** `http://143.198.153.239/api`
- **URL:** `/api/fixed/`
- **Método:** `POST`
- **Descripción:** Registra una o más vulnerabilidades como fijas.
- **Body (JSON):**
```json
   {
      "vulnerability": "CVE-2000-0431"
   }
```

### 3️⃣ **Listado de vulnerabilidades excluyendo fixeadas** ❌
- **URL DESPLEGADA:** `http://143.198.153.239/api`
- **URL:** `/api/vulnerabilities-unfixed/`
- **Método:** `GET`
- **Descripción:** Devuelve las vulnerabilidades que no han sido solucionadas, excluyendo las fixeadas.

### 4️⃣ **Resumen por severidad** 📊
- **URL DESPLEGADA:** `http://143.198.153.239/api`
- **URL:** `/api/vulnerabilities-summary/`
- **Método:** `GET`
- **Descripción:** Devuelve un resumen de la cantidad de vulnerabilidades por cada nivel de severidad.

### 5️⃣ **Eliminar vulnerabilidades (Adicional)** 🗑️
- **URL DESPLEGADA:** `http://143.198.153.239/api`
- **URL:** `/api/vulnerabilities/delete/CVE-2000-0461/`
- **Método:** `DELETE`
- **Descripción:** Elimina una vulnerabilidad de la base de datos.

---

## 🔑 **Autenticación con Token**
Para acceder a los endpoints, se implementó **autenticación mediante tokens**.
```bash
   Authorization: Token <tu-token>
```

---

## 📄 **Auditoría y Logs**
Todas las solicitudes a la API se registran en el archivo:
```
   logs/api.log
```
Para visualizar los registros:
```bash
   cat logs/api.log
```

---

## 🧪 **Ejecutando los Tests** 🔍
Se implementaron **tests automáticos** con **pytest**.

Para ejecutarlos:
```bash
   docker-compose exec api pytest
```
Esto verificará el correcto funcionamiento de los endpoints y la lógica del backend.

---

## ☁️ **Despliegue en la Nube (Digital Ocean)**
La API se encuentra desplegada en **http://143.198.153.239** **Digital Ocean** utilizando **Docker** y **MySQL**.

Pasos realizados:
1. Creación de un Droplet en Digital Ocean con Docker preinstalado.
2. Configuración del entorno y base de datos MySQL.
3. Subida de la aplicación mediante **GitHub Actions** y `docker-compose`.

---

## 📊 **Diagrama de la Solución**

El siguiente diagrama ilustra la arquitectura implementada en la nube:

![Diagrama de Arquitectura](https://tu-imagen-diagrama.com/diagrama.png)

La solución está compuesta por:
- **API en Django** corriendo en un contenedor Docker.
- **Base de datos MySQL** en un segundo contenedor.
- **Despliegue en Digital Ocean** con escalabilidad en mente.
- **Autenticación y seguridad** implementadas con tokens y auditoría de logs.

---


## 🌐 **Acceso a la Aplicación y Visualización de Datos**  

La API ha sido desplegada en la siguiente URL pública:  

🔗 **[http://143.198.153.239/](http://143.198.153.239/)**  

Desde esta dirección, se pueden consumir los diferentes endpoints de la API para gestionar vulnerabilidades.  

Además, se han desarrollado gráficos interactivos que consumen los datos expuestos por la API. Estos gráficos permiten analizar y visualizar información relevante sobre las vulnerabilidades detectadas en la infraestructura.  

Para acceder a estos gráficos y explorar la información en un entorno visual:  

📈 **[Ver Gráficos](http://143.198.153.239/)**  

Estos gráficos se actualizan en tiempo real, proporcionando una visión clara del estado de seguridad en la infraestructura monitoreada. 🚀

## 🎯 **¡Gracias por su tiempo! 😊🚀**
