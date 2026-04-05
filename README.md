# solemne1-fastapi

# Solemne 1: API de Tiempo con FastAPI y Docker

## Descripción
Este proyecto es una API sencilla desarrollada con FastAPI que entrega la fecha y hora actual en formato JSON. Implementa un flujo completo de CI/CD con GitHub Actions y contenedorización con Docker.

## Ejecución Local
1. Asegúrate de tener instalado Python 3.11+.
2. Instalar dependencias con uv: `uv sync`.
3. Ejecutar la aplicación: `uv run uvicorn main:app --reload --port 8000`.

## Ejecución con Docker
1. Construir la imagen: `docker build -t fastapi-app .`.
2. Ejecutar el contenedor: `docker run -p 8000:8000 fastapi-app`.

## Testeo de la API
Puedes probar el endpoint accediendo a `http://localhost:8000/time` desde tu navegador o usando curl:
`curl http://localhost:8000/time`