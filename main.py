from fastapi import FastAPI
from datetime import datetime

# Creamos la aplicación
app = FastAPI()


# Definimos el endpoint solicitado
@app.get("/time")
async def get_time():
    # Obtenemos la hora en formato: Año-Mes-Día Hora:Minuto:Segundo
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": ahora}
