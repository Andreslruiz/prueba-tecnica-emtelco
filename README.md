# 🖥️ Prueba Técnica - Ingeniero de Aplicaciones Full Stack 🚀

¡Hola, equipo de **Emtelco**! 👋

Soy Carlos Andres Loaiza Ruiz, y comparto mi prueba tecnica para el cargo de Ingeniero de Aplicaciones Full Stack. 🚀

## 🚀 **Endpoints de la API**

1. **Listado de vulnerabilidades** 📋
   - **URL:** `/api/vulnerabilities/`
   - **Método:** GET
   - **Descripción:** Devuelve el listado total de vulnerabilidades.

2. **Registrar vulnerabilidades fijas** ✅
   - **URL:** `/api/fixed/`
   - **Método:** POST
   - **Descripción:** Registra una o más vulnerabilidades como fijas.
   - **Body (JSON):**
     ```json
     {
        "vulnerability": "CVE-2000-0431"
     }
     ```

3. **Listado de vulnerabilidades excluyendo fixeadas** ❌
   - **URL:** `/api/vulnerabilities-unfixed/`
   - **Método:** GET
   - **Descripción:** Devuelve las vulnerabilidades que no han sido solucionadas, excluyendo las fixeadas.

4. **Resumen por severidad** 📊
   - **URL:** `/api/vulnerabilities-summary/`
   - **Método:** GET
   - **Descripción:** Devuelve un resumen de la cantidad de vulnerabilidades por cada nivel de severidad.

5. **Eliminar vulnerabilidades** 📋
   - **URL:** `/api/vulnerabilities/delete/CVE-2000-0461/`
   - **Método:** DELETE
   - **Descripción:** Elimina una vulnerabilidad de la base de datos.

---

## 🛠️ **Ejecutando los Tests** 🔍

Sigue estos pasos para ejecutar los tests de la API:

1. **Ejecutar pytest** 🔧:
   ```bash
   pytest

## 🛠️ **Ejecutando los Tests** 🔍

Sigue estos pasos para ejecutar los tests de la API:

1. **Ejecutar pytest** 🔧:
   ```bash
   pytest

## Ver los logs de la API 📄:
cat logs/api.log

