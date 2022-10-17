from fileinput import filename
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from pydantic import FilePath
from fastapi.staticfiles import StaticFiles
import uvicorn
import shutil
import os
from model import setup
from fastapi.templating import Jinja2Templates

app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):    
        return templates.TemplateResponse("index.html", {"request": request})

@app.delete('/del')
def delete():
    filePath_input = './input.csv'
    if os.path.exists(filePath_input):
        os.remove(filePath_input)
    filePath_output = os.curdir + 'output.csv'
    if os.path.exists(filePath_output):
        os.remove(filePath_output)

@app.post('/load_data')
def root(csv_file: UploadFile = File(...)):
    try:
        with open(f"{csv_file.filename}", "wb") as buffer:
            shutil.copyfileobj(csv_file.file, buffer)
            os.rename(csv_file.filename, 'input.csv')
            return RedirectResponse(url="/train", status_code=303)
    except:
        return {"file_name": "error"}
    # content = await csv_file.read()
    # print(content)


@app.get('/train')
def train():
    setup()
    return RedirectResponse(url="/output", status_code=303)

@app.get('/output')
def download_file():
    file_path = os.curdir + "output.csv"
    return FileResponse(path=file_path, filename='output.csv')


if __name__ == '__main__':
    uvicorn.run("app:app",  host="0.0.0.0", port=5000, workers=1,reload=True)