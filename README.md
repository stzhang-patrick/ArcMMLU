# ArcMMLU—面向图书馆与信息科学(LIS)的中文大语言模型评测基准



<p align="center"> <img src="fig/banner.jpg" style="width: 100%;" id="title-icon">       </p>

<h4 align="center">
    <p>
        <b>简体中文</b> |
        <a href="https://github.com/stzhang-patrick/ArcMMLU/blob/main/README_EN.md">English</a> 
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="#" target="_blank" style="margin-right: 15px; margin-left: 10px">论文</a> •
🏆 <a href="#" target="_blank"  style="margin-left: 10px">排行榜</a> • 
🤗 <a href="#" target="_blank" style="margin-left: 10px">数据集</a>
</p>


## 简介

ArcMMLU是一个专为图书馆与信息科学（Library & Information Science, LIS）打造的中文大语言模型评测基准，旨在评估大语言模型在LIS学科领域的知识掌握和推理能力，其中涵盖了档案学、数据科学、图书馆学和信息学等四个关键细分领域。

需要特别说明的是，ArcMMLU的命名来源于我们之前的大语言模型研究项目—— [ArcGPT](https://arxiv.org/abs/2307.14852)，这一项目主要针对档案学。随后，我们的研究视野从档案学拓展至更广泛的信息管理领域，但我们仍然保留了ArcMMLU这一称谓。因此，ArcMMLU不仅仅是档案学的评测基准，它是面向整个LIS学科的综合评测工具。

出于通用性、便捷性的考虑，ArcMMLU选择了与CMMLU一致的数据格式。同时，基于CMMLU项目，我们提供了匹配的评测代码。对已在CMMLU上评测过的模型，进行ArcMMLU的评测将会变得格外简便。特别感谢 [CMMLU---中文多任务语言理解评估](https://github.com/haonan-li/CMMLU) 项目为中文大语言模型评测所作出的贡献。我们希望ArcMMLU能作为其在细分领域的有力补充，为中文大语言模型评测带来更多的细节与深度。


<p align="center"> <img src="fig/main.jpg" style="width: 65%;" id="title-icon">       </p>

## 排行榜

以下表格显示了模型在 zero-shot 和 five-shot 下的表现。如果您想贡献您的模型结果，请与我们联系或直接提交拉取请求。

### Zero-shot


| 模型                                                                          | 档案学 | 数据科学 | 图书馆学 | 信息学 | 平均分 |
|-------------------------------------------------------------------------------|-------|---------|---------|-------|-------|
| GPT4 (gpt-4-0613)                                                             | 66.38 | 82.12 | 66.79 | 78.55 | 73.46 |
| [Qwen-14B](https://github.com/QwenLM/Qwen)                                    | 66.65 | 71.51 | 63.06 | 71.21 | 68.11 |
| [Baichuan2-13B](https://github.com/baichuan-inc/Baichuan2)                    | 61.59 | 65.58 | 61.57 | 66.49 | 63.81 |
| [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B)                           | 61.82 | 65.64 | 59.58 | 66.67 | 63.43 |
| [Qwen-7B](https://github.com/QwenLM/Qwen)                                     | 59.78 | 64.31 | 56.47 | 63.68 | 61.06 |
| ChatGPT (gpt-3.5-turbo)                                                       | 52.37 | 65.64 | 52.61 | 66.19 | 59.20 |
| [InternLM-20B](https://github.com/InternLM/InternLM)                          | 53.82 | 61.37 | 55.72 | 63.14 | 58.51 |
| [Baichuan2-7B](https://github.com/baichuan-inc/Baichuan2)                     | 56.08 | 61.11 | 55.72 | 61.11 | 58.50 |
| [Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B)                  | 54.41 | 57.17 | 54.48 | 61.05 | 56.78 |
| [XVERSE-13B](https://github.com/xverse-ai/XVERSE-13B)                         | 53.37 | 56.70 | 57.21 | 59.62 | 56.73 |
| [InternLM-7B](https://github.com/InternLM/InternLM)                           | 51.88 | 59.97 | 51.37 | 61.29 | 56.13 |
| [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)                           | 52.06 | 56.97 | 49.00 | 53.70 | 52.93 |
| [educhat-base-002-13b](https://github.com/icalk-nlp/EduChat)                  | 47.85 | 52.84 | 48.01 | 57.47 | 51.54 |
| [Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)                    | 49.21 | 46.36 | 45.27 | 48.69 | 47.38 |
| [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)                             | 43.06 | 46.96 | 38.81 | 47.91 | 44.19 |
| [Ziya-LLaMA-13B-v1.1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1.1)   | 37.32 | 41.69 | 40.05 | 47.43 | 41.63 |


### Five-shot

| 模型                                                                          | 档案学 | 数据科学 | 图书馆学 | 信息学 | 平均分 |
|-------------------------------------------------------------------------------|-------|---------|---------|-------|-------|
| GPT4 (gpt-4-0613)                                                             | 68.41 | 81.99 | 70.40 | 79.51 | 75.08 |
| [Qwen-14B](https://github.com/QwenLM/Qwen)                                    | 67.24 | 72.85 | 64.80 | 71.39 | 69.07 |
| [Baichuan2-13B](https://github.com/baichuan-inc/Baichuan2)                    | 62.00 | 66.91 | 61.44 | 66.07 | 64.11 |
| [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B)                           | 61.91 | 63.44 | 61.69 | 65.77 | 63.20 |
| [XVERSE-13B](https://github.com/xverse-ai/XVERSE-13B)                         | 60.33 | 62.98 | 60.20 | 65.53 | 62.26 |
| [Qwen-7B](https://github.com/QwenLM/Qwen)                                     | 58.74 | 65.31 | 59.20 | 64.70 | 61.99 |
| [Baichuan2-7B](https://github.com/baichuan-inc/Baichuan2)                     | 59.56 | 63.51 | 59.95 | 63.26 | 61.57 |
| ChatGPT (gpt-3.5-turbo)                                                       | 53.95 | 68.18 | 53.86 | 66.31 | 60.57 |
| [Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B)                  | 56.12 | 61.24 | 59.33 | 62.19 | 59.72 |
| [InternLM-20B](https://github.com/InternLM/InternLM)                          | 54.77 | 61.04 | 56.84 | 61.77 | 58.60 |
| [InternLM-7B](https://github.com/InternLM/InternLM)                           | 50.75 | 59.24 | 50.50 | 59.44 | 54.98 |
| [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)                           | 52.78 | 53.97 | 48.76 | 51.85 | 51.84 |
| [Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)                    | 50.70 | 50.63 | 46.64 | 52.63 | 50.15 |
| [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)                             | 39.99 | 40.23 | 36.57 | 41.88 | 39.67 |



## 数据示例

数据集内的每个问题均为四选一的选择题，其中仅有一个选项为正确答案。数据采用逗号分隔，并保存为.csv文件格式。以下是数据样例：

```bash
# 档案学
问题: 档案与图书、文献资料相比，其特有属性是( )。
A.原始记录性
B.知识性
C.信息性
D.服务型
答案: A

# 数据科学
问题: 在下列哪种情况下，我们通常使用回归分析？( )
A.当我们想预测一个连续的变量，例如人的身高。
B.当我们想预测一个离散的变量，例如人的婚姻状态。
C.当我们想预测一个分类变量，例如人的性别。
D.当我们有一组变量，并且想找出它们之间的关系。
答案: A

# 图书馆学
问题: 《中图法》中基本大类由22个字母表示，“E”和“O”分别表示的是( )。
A.军事，数理科学和化学
B.文学，环境科学
C.语言文学、天文学
D.经济，法律
答案: A

# 信息学
问题: 在信息分布的规律和特征中，揭示论文在科学期刊中的分布规律的定律是( )。
A.马太效应
B.布拉德福定律
C.齐夫定律
D.洛特卡定律
答案: B
```

## 使用方法

要在您的项目中使用我们的代码，请将存储库克隆到本地计算机：

```bash
git clone https://github.com/stzhang-patrick/ArcMMLU.git
cd ArcMMLU/src
```

## 数据

我们根据每个评测维度在 data/dev 和 data/test 目录中提供了开发和测试数据集。

## 引用

```
@misc{zhang2023arcgpt,
    title={ArcGPT: A Large Language Model Tailored for Real-world Archival Applications}, 
    author={Shitou Zhang and Jingrui Hou and Siyuan Peng and Zuchao Li and Qibiao Hu and Ping Wang},
    year={2023},
    eprint={2307.14852},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
## 许可证

ArcMMLU数据集采用
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).