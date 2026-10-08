from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI()
htmltemp = Jinja2Templates(directory="Templates")




@app.get("/homepage", response_class=HTMLResponse)
async def get_homepage(request: Request):
    return htmltemp.TemplateResponse(request, 'index.html', {"request": request})


@app.post("/translate", response_class=HTMLResponse)
async def post_translation():
    return 0;