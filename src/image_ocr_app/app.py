# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: app.py
# @time: 2024/10/24 16:29
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import os
from typing import List
from cnocr import CnOcr

app = FastAPI()

# 配置允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 上传文件的保存目录
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 使用Jinja2模板引擎
templates = Jinja2Templates(directory="templates")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

ocr = CnOcr(det_model_name='naive_det',
            rec_vocab_fp='static/label.txt',
            rec_model_fp='static/ch_captcha.onnx')


# 图片上传页面
@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


# 处理图片上传并返回图片的内容
@app.post("/upload/")
async def upload_image(files: List[UploadFile] = File(...)):
    # 限制文件大小（10MB以内）
    MAX_SIZE = 10 * 1024 * 1024
    uploaded_files = []
    file_urls = []
    ocr_results = []

    for file in files:
        content = await file.read()
        if len(content) > MAX_SIZE:
            raise HTTPException(status_code=413, detail="File too large")

        file_location = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(content)

        uploaded_files.append(file.filename)
        file_path = f"{UPLOAD_DIR}/{file.filename}"
        file_urls.append(file_path)

        # OCR识别，使用训练好的CnOCR模型来识别图片中的文字
        out = ocr.ocr(file_path)
        print(out)
        ocr_results.append(out[0]['text'])

    return {"uploaded_files": uploaded_files, "file_urls": file_urls, "ocr_results": ocr_results}
