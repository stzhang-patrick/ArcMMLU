# ArcMMLU—面向图书馆与情报学(LIS)的中文综合评测基准

## 简介

ArcMMLU是一个面向图书馆与情报学（Library and Information Science, LIS）的中文综合评测基准，专门用于评估语言模型在中文LIS学科领域的知识和推理能力，涵盖了档案学、数据科学、图书馆学和信息学四个评测维度。

值得一提的是，ArcMMLU的名字起源自我们面对档案学的大语言模型研究项目，ArcGPT。在此之后，我们的研究范围从档案学扩大到了整个图书馆与信息科学（Library & Information Science），但是我们仍然沿用了ArcMMLU的名字。因此，ArcMMLU是面向LIS学科的综合评测基准，包括但并不仅限于档案学。

出于通用性、便捷性的考虑，在设计ArcMMLU时，我们采用了与CMMLU相同的数据集格式，并基于CMMLU项目提供了相应的评测代码。这意味着如果某个大型语言模型已经完成了CMMLU的评测，那么只需进行少量修改就可以快速进行ArcMMLU的评测。

特别感谢[CMMLU---中文多任务语言理解评估](https://github.com/haonan-li/CMMLU#cmmlu---%E4%B8%AD%E6%96%87%E5%A4%9A%E4%BB%BB%E5%8A%A1%E8%AF%AD%E8%A8%80%E7%90%86%E8%A7%A3%E8%AF%84%E4%BC%B0)项目为中文大型语言模型评测所作出的贡献。我们希望ArcMMLU能够成为中文大型语言模型评测的细分领域补充，进一步完善、丰富中文大型语言模型评测。

## 排行榜（未排序）

以下表格显示了模型在 five-shot 和 zero-shot 下的表现。如果您想贡献您的模型结果，请与我们联系或直接提交拉取请求。

### Five-shot

| 模型         | 档案学 | 数据科学 | 图书馆学 | 信息学 | 平均分 |
| ------------ | ------ | -------- | -------- | ------ | ------ |
| ChatGLM2-6B  | 52.73  | 54.10    | 51.85    | 48.63  | 51.83  |
| BATGPT-15B   | 44.15  | 49.57    | 45.94    | 43.53  | 45.80  |
| XVERSE-13B   | 60.28  | 63.18    | 65.41    | 60.32  | 62.30  |
| InternLM-7B  | 51.33  | 61.11    | 60.33    | 51.24  | 56.00  |
| Baichuan-7B  | 50.70  | 50.63    | 52.63    | 46.64  | 50.15  |
| Baichuan-13B | 56.12  | 61.24    | 62.19    | 59.33  | 59.72  |

### Zero-shot

| 模型         | 档案学 | 数据科学 | 图书馆学 | 信息学 | 平均分 |
| ------------ | ------ | -------- | -------- | ------ | ------ |
| ChatGLM2-6B  | 52.19  | 56.70    | 53.82    | 48.88  | 52.90  |
| BATGPT-15B   | 48.31  | 54.30    | 53.35    | 45.27  | 50.31  |
| XVERSE-13B   | 53.68  | 55.64    | 58.84    | 56.34  | 56.13  |
| InternLM-7B  | 52.96  | 59.91    | 59.62    | 51.24  | 55.95  |
| Baichuan-7B  | 49.21  | 46.36    | 48.69    | 45.27  | 47.38  |
| Baichuan-13B | 54.41  | 57.17    | 61.05    | 54.48  | 56.78  |

## 数据格式

数据集中的每个问题都是一个多项选择题，有4个选项，只有一个选项是正确答案。数据以逗号分隔的.csv文件形式存在。 这里是数据格式的示例：

```
0,2020年6月20日，第十三届全国人大常委会第十九次会议审议通过了新修订的《中华人民共和国档案法》，国家主席习近平签署第四十七号主席令予以公布，自( )起正式施行。,2020年6月20日,2020年7月1日,2021年1月1日,2021年6月20日,C
```

## 使用方法

要在您的项目中使用我们的代码，请将存储库克隆到本地计算机：

```
git clone https://github.com/stzhang-patrick/ArcMMLU.git
cd ArcMMLU/src
```

## 数据

我们根据每个评测维度在data/dev和data/test目录中提供了开发和测试数据集。

