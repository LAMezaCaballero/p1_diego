#istalar python-multipart, fastapi, fastparquet,pyarrow, uvicorn, 

from typing import Union

from fastapi import FastAPI, File, UploadFile
from fastparquet import ParquetFile
import json
import pandas as pd


from routers import horasjugadas #importar routers

app = FastAPI()

app.include_router(horasjugadas.router) #anexar router en el api


@app.get("/")
async def read_root():
    
    return {"Hello": "World2"}
