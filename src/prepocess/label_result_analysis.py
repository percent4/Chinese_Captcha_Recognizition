# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: label_result_analysis.py
# @time: 2024/9/19 20:28
import json
from collections import defaultdict

char_cnt_dict = defaultdict(int)

# 读取Label-Studio的标注结果
# with open('../../data/project-5-at-2024-09-29-03-11-dfa34688.json', 'r') as f:
#     data = json.loads(f.read())
#
# for i in range(len(data)):
#     annotation_text = data[i]['annotations'][0]['result'][0]['value']['text'][0]
#     if '串' in annotation_text:
#         print(data[i])
#     for char in annotation_text:
#         char_cnt_dict[char] += 1

# 读取自己标注的数据
with open('../../data/4char_tagged_content.txt', 'r') as f:
    lines = [_.strip() for _ in f.readlines()]

for line in lines:
    tagged_content = line.split('\t')[-1]
    for char in tagged_content:
        char_cnt_dict[char] += 1

print(f"共有标注样本个数：{len(lines)}")

# 保存数据
with open('../../data/chars.txt', 'w') as f:
    f.write('\n'.join(sorted(list(char_cnt_dict.keys()))))

# 将char_cnt_dict按照value值进行排序
sorted_char_cnt_dict = dict(sorted(char_cnt_dict.items(), key=lambda x: x[1], reverse=True))
with open('../../data/char_cnt_dict.json', 'w') as f:
    f.write(json.dumps(sorted_char_cnt_dict, indent=4, ensure_ascii=False))


one_cnt = 0
for k, v in char_cnt_dict.items():
    if v == 1:
        print(k, v)
        one_cnt += 1
print("出现次数为1的字符个数为:", one_cnt)

