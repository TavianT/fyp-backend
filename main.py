from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    return {"content_type": file.content_type, "file_name": file.filename}