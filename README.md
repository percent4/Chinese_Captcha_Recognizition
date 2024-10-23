本项目主要使用`CnOCR`来训练自己的OCR模型，用于汉字验证码破解。

## 验证码介绍

### 三汉字验证码

1. 生成验证码，使用脚本生成，参考`src/preprocess/gen_captcha_v1.py`文件
2. 验证码样本如下：

![4003.jpg](https://s2.loli.net/2024/10/23/ilyHSdeOJLz6jus.jpg)

## 破解思路

1. 利用Label Studio标注平台或者自己写的标注平台来人工标注验证码
2. 保证标注的数据集的数量与质量，一般汉字验证码需要几千个以上的标注样本
3. 使用`CnOCR`来训练自己的OCR模型
4. 使用训练好的模型来识别验证码

## 如何训练模型

### 训练数据格式

1. 三汉字验证码共标注9033个样本，按训练集与验证集8:2划分，其中训练集样本7162个，验证集样本1827个。

### 模型训练

## 模型效果验证

### 三汉字验证码

验证集共1827个样本，识别正确率为91.24%。

## 参考网站

1. `CnOCR`脚本工具: [https://cnocr.readthedocs.io/zh-cn/stable/command/](https://cnocr.readthedocs.io/zh-cn/stable/command/)