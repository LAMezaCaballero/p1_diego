from fastapi import APIRouter, UploadFile, File
import pyarrow as pa
import pandas as pd
import json

router = APIRouter() # ahora se importa en main el router

@router.post("/upload/")

async def upload_file(file: UploadFile = File(...)):
    # Leer el archivo Parquet con codificación UTF-8
    df = pa.parquet.read_table(file.file, encoding="utf-8")

    # Procesar el DataFrame (opcional)
    # ...

    # Regresar una respuesta
    return {"message": "Archivo subido correctamente"}