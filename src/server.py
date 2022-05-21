from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

app = FastAPI()


@app.post("/upload")
async def upload(image_file: UploadFile = File(...)):
    image = np.array(Image.open(BytesIO(await image_file.read())))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return {"message": "Successfully Upload"}
