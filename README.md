本项目主要使用`CnOCR`来训练自己的OCR模型，用于汉字验证码破解。

## 验证码介绍

### 三汉字验证码

1. 生成验证码，使用脚本生成，参考`src/preprocess/gen_captcha_v1.py`文件，完整数据参考`data/corpus`文件夹
2. 验证码样本如下：

![4003.jpg](https://s2.loli.net/2024/10/23/ilyHSdeOJLz6jus.jpg)

三汉字验证码共标注9033个样本，按训练集与验证集8:2划分，其中训练集样本7162个，验证集样本1827个。

### 四汉字验证码

1. 生成验证码，使用脚本生成，参考`src/preprocess/gen_captcha_v2.py`文件，完整数据参考`data/4char_corpus`文件夹
2. 验证码样本如下：

![](https://s2.loli.net/2024/10/23/GgrLlDnQ92TPuI6.png)

四汉字验证码共标注2047个样本，按训练集与验证集8:2划分，其中训练集样本1646个，验证集样本399个。

## 破解思路

1. 利用Label Studio标注平台或者自己写的标注平台来人工标注验证码
2. 保证标注的数据集的数量与质量，一般汉字验证码需要几千个以上的标注样本
3. 使用`CnOCR`来训练自己的OCR模型
4. 使用训练好的模型来识别验证码

## 模型训练

使用`CnOCR`工具包来训练自己的OCR模型，主要步骤如下：

1. 对图片进行标注，形成标注数据，标注平台可以使用`Label Studio`或者自己写的标注平台（参考`src/image_tagging`目录）
2. 使用`src/prepocess/get_train_val_data.py`得到训练数据train.tsv与验证数据dev.tsv
3. 模型训练命令:

```commandline
cnocr train -m densenet_lite_136-gru --index-dir data/4char_captcha --train-config-fp docs/examples/train_config_gpu.json
```

## 模型效果验证

导出onnx模型，命令如下：

```commandline
cnocr export-onnx -m densenet_lite_136-gru -v /workspace/code/CnOCR/data/4char_captcha/label.txt -i /workspace/code/CnOCR/runs/CnOCR-Rec/pgyahgqm/checkpoints/cnocr-v2.3-densenet_lite_136-gru-epoch=093-val-complete_match-epoch=0.9148.ckpt -o /workspace/code/CnOCR/runs/CnOCR-Rec/pgyahgqm/checkpoints/ch_captcha.onnx
```

模型评估，命令如下：

```commandline
cnocr evaluate -p /workspace/code/CnOCR/runs/CnOCR-Rec/pgyahgqm/checkpoints/ch_captcha.onnx -v /workspace/code/CnOCR/data/4char_captcha/label.txt -i ./data/4char_captcha/dev.tsv --image-folder ./data/4char_captcha/4char_corpus
```

| 验证码类型 |验证码数量| 正确率 | cer   |
|-------|---|---|-------|
| 三汉字   |1827|91.24%| 0.032 |
| 四汉字   |399|88.72%| 0.031 |


### 可视化: OCR识别页面

功能：实现验证码图片的上传与OCR识别

![验证码上传与识别页面](https://s2.loli.net/2024/10/25/lqxK6VJyi5O9gA2.png)

## 参考网站

1. `CnOCR`脚本工具: [https://cnocr.readthedocs.io/zh-cn/stable/command/](https://cnocr.readthedocs.io/zh-cn/stable/command/)
2. https://zhuanlan.zhihu.com/p/2845583696 