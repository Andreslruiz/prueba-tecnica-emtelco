# Usa una imagen oficial de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto
COPY requirements.txt .
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto para Django
EXPOSE 8000

# Comando por defecto para ejecutar la app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
