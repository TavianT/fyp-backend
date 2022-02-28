from fastapi import FastAPI, File, UploadFile

from flower_prediction import classify_image

import uuid

app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    filename = f'/tmp/{str(uuid.uuid4())}.jpg'
    contents = await file.read()
    with open(filename, "wb") as img_file:
        img_file.write(contents)
    return classify_image(filename)