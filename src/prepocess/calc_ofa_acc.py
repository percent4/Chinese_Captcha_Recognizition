# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: calc_ofa_acc.py
# @time: 2024/10/22 17:24
with open('../image_tagging/tagged_content.txt', 'r') as f:
    content = [_.strip() for _ in f.readlines()]

correct_cnt = 0
for line in content:
    cells = line.split('\t')
    origin_text, new_text = cells[2], cells[3]
    if origin_text == new_text:
        correct_cnt += 1

print(correct_cnt, len(content))
print(f"OFA accuracy: {correct_cnt / len(content)}")
