from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    return {"file_size": len(file), "file_name": file.filename}