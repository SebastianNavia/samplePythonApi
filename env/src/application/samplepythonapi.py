

from fastapi import FastAPI

app: FastAPI = FastAPI(
    title ="samplePythonApi"
    description ="USBCS202401"

)

################################

@app.get(
    "/operacionGet",
    summary = "Operacion Get",
    tags=[Get])
async def operacion_get(dato_entrada: str):
    return dato_entrada