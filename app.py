from fileinput import filename
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import FilePath
import uvicorn
import shutil
import os
from model import setup
app = FastAPI(debug=True)


@app.delete('/del')
def delete():
    filePath_input = './input.csv'
    if os.path.exists(filePath_input):
        os.remove(filePath_input)
    filePath_output = './output.csv'
    if os.path.exists(filePath_output):
        os.remove(filePath_output)


@app.post('/load_data')
def root(file: UploadFile = File(...)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        os.rename(file.filename, 'input.csv')
        return {"file_name": file.filename}


@app.get('/train')
def train():
    setup()


@app.get('/output')
def download_file():
    file_path = "/home/tanav/test/fastapi/output.csv"
    return FileResponse(path=file_path, filename='output.csv')


if __name__ == '__main__':
    uvicorn.run(app,  host="127.0.0.1", port=5000, workers=1)
