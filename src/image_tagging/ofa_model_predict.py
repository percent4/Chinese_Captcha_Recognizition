# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: ofa_model_predict.py
# @time: 2024/10/23 14:34
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.outputs import OutputKeys

# ModelScope Library >= 1.2.0
ocr_recognize = pipeline(Tasks.ocr_recognition, model='damo/ofa_ocr-recognition_general_base_zh', model_revision='v1.0.2')
with open('ofa_ocr_predict.txt', 'a', encoding='utf-8') as f:
    for i in range(3000):
        file_name = f'{i}.jpg'
        result = ocr_recognize(f'/workspace/code/OFA_OCR/corpus/{file_name}')
        pred_text = result[OutputKeys.TEXT][0]
        print(f"{file_name}\t{pred_text}")
        f.write(f"{file_name}\t{pred_text}\n")
