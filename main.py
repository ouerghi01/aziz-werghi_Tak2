from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from FAQretrieval import find_best_reponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
@app.get('/',response_class=HTMLResponse)
async def main_page(request:Request):
    return templates.TemplateResponse("index.html",{
        "request":request
    })
@app.post('/answer_to_question')
async def reponsed(request: Request, question: str = Form(...)):
    try:
        best_answer = find_best_reponse(question)
        if not best_answer:
            return "<p> No suitable answer found. </p>"
        return best_answer
    except Exception as e:
        return f"<p> error {e}</p>"
