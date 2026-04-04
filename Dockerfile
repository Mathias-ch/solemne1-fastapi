# 1. Utilizar una imagen base de Python [cite: 26]
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

ENV TZ="America/Santiago"

# 2. Copiar los archivos necesarios al contenedor [cite: 27]
# Copiamos primero el archivo de dependencias para optimizar la construcción
COPY requirements.txt .

# 3. Instalar las dependencias de Python [cite: 28]
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código (main.py)
COPY . .

# 4. Exponer el puerto 8000 [cite: 33]
EXPOSE 8000

# 5. Definir el comando para ejecutar la aplicación con uvicorn [cite: 34, 21]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]