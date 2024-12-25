from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from pydantic import BaseModel
from FAQretrieval import find_best_response
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get('/',response_class=HTMLResponse)
async def main_page(request:Request):
    async def main_page(request: Request):
        """
        Handles the main page request and returns the rendered index.html template.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            TemplateResponse: The response containing the rendered HTML template.
        """
    return templates.TemplateResponse("index.html",{
        "request":request
    })
@app.post('/answer_to_question')
async def get_best_answer(request: Request, question: str = Form(...)):
    """
    Endpoint to get the best answer to a given question.

    Args:
        request (Request): The request object.
        question (str, Form): The question for which an answer is sought.

    Returns:
        str: The best answer found or an error message if no suitable answer is found or an exception occurs.

    Raises:
        Exception: If an error occurs during the process of finding the best answer.
    """
    try:
        best_answer = find_best_response(question)
        if not best_answer:
            return "<p> No suitable answer found. </p>"
        return best_answer
    except Exception as e:
        return f"<p> error {e}</p>"
if __name__ == "__main__":
    uvicorn.run("main:main", host="0.0.0.0", port=8000, reload=True)
