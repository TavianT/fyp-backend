from fastapi import FastAPI, File, UploadFile

from flower_prediction import classify_image

import uuid
import cv2

app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    filename = f'tmp_images/{str(uuid.uuid4())}.jpg'
    # img = cv2.imread(file)
    # cv2.imwrite(filename, img)
    contents = await file.read()
    with open(filename, "wb") as img_file:
        img_file.write(contents)
    return classify_image(filename)