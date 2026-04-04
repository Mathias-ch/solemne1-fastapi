from fastapi.testclient import TestClient
from main import app

# Creamos el cliente de pruebas que "simula" un navegador
client = TestClient(app)


def test_read_time():
    """
    Prueba que el endpoint /time responda correctamente (Status 200)
    y que el formato del JSON sea el esperado.
    """
    response = client.get("/time")

    # 1. Verificamos que la conexión sea exitosa (Código 200)
    assert response.status_code == 200

    # 2. Verificamos que la respuesta sea un JSON y contenga la clave "time"
    data = response.json()
    assert "time" in data

    # 3. Verificamos que el valor no esté vacío
    assert isinstance(data["time"], str)
    assert len(data["time"]) > 0
