from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api_functions import developer, userdata, userForGenre, best_developer_year, developer_reviews_analysis

router1 = APIRouter()
router2 = APIRouter()
router3 = APIRouter()
router4 = APIRouter()
router5 = APIRouter()

@router1.get("/developer/{desarrollador}")
def read_developer(desarrollador: str):
    result = developer(desarrollador)
    return JSONResponse(content=result)

@router2.get("/userdata/{user_id}")
def read_userdata(user_id: str):
    result = userdata(user_id)
    return JSONResponse(content=result)

@router3.get("/UserForGenre/{genero}")
def read_user_for_genre(genero: str):
    result = UserForGenre(genero)
    return JSONResponse(content=result)

@router4.get("/best_developer_year/{year}")
def read_best_developer_year(year: int):
    result = best_developer_year(year)
    return JSONResponse(content=result)

@router5.get("/developer_reviews_analysis/{desarrolladora}")
def read_developer_reviews_analysis(desarrolladora: str):
    result = developer_reviews_analysis(desarrolladora)
    return JSONResponse(content=result)
