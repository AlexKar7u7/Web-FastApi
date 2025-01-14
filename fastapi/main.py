from typing import Union

from fastapi import FastAPI, Request


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="index.html", #context={"nombre": "pepe"}                                                      
    )

@app.get("/registrarse", response_class=HTMLResponse)
async def registrarse(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="Registrarse.html", #context={"nombre": "pepe"}                                                      
    )

@app.get("/recursos", response_class=HTMLResponse)
async def recursos(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="Recursos.html", #context={"nombre": "pepe"}                                                      
    )
    
    
@app.get("/utilesrise", response_class=HTMLResponse)
async def utilesrise(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="UtilesMHRise.html", #context={"nombre": "pepe"}                                                      
    )