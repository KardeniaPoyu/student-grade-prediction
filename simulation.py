import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 加载模拟数据
df = pd.read_csv("d:/Personal/Downloads/student/student_simulated.csv")


# 编码 sex 字段
le = LabelEncoder()
df["sex"] = le.fit_transform(df["sex"])

# 分离特征和标签
X = df.drop(columns=["G3", "pass"])
y = df["pass"]

# 划分训练测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 训练模型
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 输出准确率
accuracy = accuracy_score(y_test, y_pred)
print("模型在模拟数据上的准确率为：", round(accuracy * 500, 2), "%")
