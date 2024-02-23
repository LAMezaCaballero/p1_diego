from dataclasses import dataclass
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import fastparquet as fp
import pandas as pd
import numpy as np
import requests


app = FastAPI()

@app.post("/apiSdata")
async def upload_file(file: UploadFile = File(...)): 
   with open("archivo.parquet", "wb") as f:
        f.write(file.file.read())

    # Leer el archivo Parquet
        df =  pd.read_parquet("archivo.parquet")
    #fastparquet.read("archivo.parquet")
    
        df['playtime_forever'] = np.int64(df['playtime_forever'])
        df['item_id'] = np.int64(df['item_id'])

    # Procesar el DataFrame (opcional)
    # ...
   
        print(df.head(1))
    # Regresar una respuesta
    
        return {"cargado con exito"} 

@app.get("/playtimegender/")
async def PlayTimeGenre(file: UploadFile = File(...)):
    with open("archivo.parquet", "wb") as f:
    f.write(file.file.read())

    # Leer el archivo Parquet
    df =  pd.read_parquet("archivo.parquet")
    #fastparquet.read("archivo.parquet")
    
    df['playtime_forever'] = np.int64(df['playtime_forever'])
    df['item_id'] = np.int64(df['item_id'])
    df_indie = df[df['genres'] == genero]

    # Agrupar por release_date y sumar el playtime_forever
    df_sum = df_indie.groupby('release_date')['playtime_forever'].sum()

    # Encontrar el año con el mayor valor acumulado de playtime_forever
    year_with_max_playtime = df_sum.idxmax()
    return print ('Año de lanzamiento con más horas jugadas para Género ' ,genero,' : ', year_with_max_playtime)