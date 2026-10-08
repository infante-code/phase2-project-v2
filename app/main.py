from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


app = FastAPI()

Books = [
    {
        "title1": "One",
        "title2": "Two"
    }
]


@app.get("/books")
async def getAllBooks():
    return Books