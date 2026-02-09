from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import jinja2
app = FastAPI()



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# def read_root():
#     return {"Hello fastAPIIIII"}

@app.get("/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse(request=request, name="landingpage.html")


@app.get("/valentinepage", response_class=HTMLResponse)
def valentinepage(request: Request):
    return templates.TemplateResponse(request=request, name="valentinepage.html")

@app.get("/thankyou", response_class=HTMLResponse)
def thankyou(request: Request):
    return templates.TemplateResponse(request=request, name="thankyou.html")
