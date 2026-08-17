# Data

本项目使用 UCI Machine Learning Repository 的 **Student Performance** 数据集（Dataset ID: 320）。数据来自葡萄牙两所学校，包含学生的学习、家庭、社会因素以及数学/葡萄牙语课程成绩。

来源：UCI Machine Learning Repository
DOI: 10.24432/C5TG7T
许可证：CC BY 4.0

## 下载数据

运行项目根目录下的命令：

```bash
python src/download_data.py
```

脚本会通过 `ucimlrepo` 获取数据，并保存为：

```text
data/student_performance.csv
```

> 原始数据包含 649 名学生记录。正式分析时，我们会明确区分特征变量与 G1/G2/G3 成绩变量，避免数据泄漏。
