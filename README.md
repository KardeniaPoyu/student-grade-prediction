# student-grade-prediction
中央民族大学22级《机器学习导论》期末大作业，预测学生成绩的机器学习项目

# 🎓 学生学业成绩预测（Student Grade Prediction）

本项目使用机器学习方法，基于葡萄牙中学学生的行为与背景数据，预测其是否能够顺利通过课程，并探索影响学生成绩的关键因素。

---

## 📁 数据来源

- 数据集：UCI Student Performance Dataset  
- 链接：[https://archive.ics.uci.edu/ml/datasets/Student+Performance](https://archive.ics.uci.edu/ml/datasets/Student+Performance)  
- 数据文件：`student-mat.csv`（数学课程成绩数据）

---

## 🎯 项目目标

- 将学生期末成绩 G3 转换为是否“及格”的二分类任务（≥10 为及格）
- 构建多种机器学习模型（逻辑回归、决策树、随机森林）
- 对比模型性能指标（Accuracy、F1-score 等）
- 分析影响成绩的主要因素（特征重要性）

---

## 🔧 使用的技术

- Python 3.9+
- Jupyter Notebook
- Pandas、NumPy
- Scikit-learn
- Seaborn / Matplotlib

---

## 📊 模型结果示例

| 模型 | 准确率 | F1 分数 |
|------|--------|---------|
| Logistic Regression | 0.79 | 0.83 |
| Decision Tree        | 0.77 | 0.79 |
| Random Forest        | 0.84 | 0.87 |

---

## 📈 特征重要性分析（基于随机森林）

- G2（第二次考试成绩）
- G1（第一次考试成绩）
- failures（曾不及格次数）
- studytime（每周学习时间）
- goout（外出社交频率）

---

## 📁 文件说明

| 文件名 | 说明 |
|--------|------|
| `student_prediction.py` | 项目核心代码（可直接运行） |
| `student-mat.csv`          | 数据文件（UCI公开数据）     |
| `report.docx`              | 大作业报告文档（Word版）   |
| `README.md`                | 本项目说明文件               |

---

## 📌 说明

本项目仅作为课程作业，数据及代码均为学习与研究用途，非商业使用。

