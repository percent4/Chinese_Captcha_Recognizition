# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: get_train_val_data.py
# @time: 2024/9/19 22:48
import csv
import json

id_lexicon_dict = {}

# 读取Label-Studios标注数据
# with open('../../data/project-5-at-2024-09-29-03-11-dfa34688.json', 'r') as f:
#     data = json.loads(f.read())
#
# for i in range(len(data)):
#     file_id = int(data[i]['file_upload'].split('-', maxsplit=1)[1].split('.')[0])
#     annotation_text = data[i]['annotations'][0]['result'][0]['value']['text'][0]
#     id_lexicon_dict[file_id] = annotation_text

# 读取自己标注的数据
with open('../../data/4char_tagged_content.txt', 'r') as f:
    lines = [_.strip() for _ in f.readlines()]

for line in lines:
    file_id = int(line.split('\t')[1].split('.')[0])
    tagged_content = line.split('\t')[-1]
    id_lexicon_dict[file_id] = tagged_content

# 获取cnocr训练格式的数据
cnocr_train_data, cnocr_test_data = [], []
for _id, lexicon in id_lexicon_dict.items():
    if _id % 10 <= 1:
        cnocr_test_data.append([f"{_id}.jpg", ' '.join([_ for _ in lexicon])])
    else:
        cnocr_train_data.append([f"{_id}.jpg", ' '.join([_ for _ in lexicon])])

# 写入文件
with open('../../data/train.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(cnocr_train_data)

with open('../../data/dev.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(cnocr_test_data)

