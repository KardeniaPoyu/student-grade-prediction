import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ========== 第一步：读取数据 ==========
df = pd.read_csv("D:/Personal/Downloads/student/student-mat.csv", sep=';')

# ========== 第二步：创建标签列（是否及格） ==========
df["pass"] = (df["G3"] >= 10).astype(int)
df_features = df.drop(columns=["G3"])  # 可选保留 G1 和 G2

# ========== 第三步：Label Encoding 所有类别变量 ==========
label_encoders = {}
for col in df_features.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df_features[col] = le.fit_transform(df_features[col])
    label_encoders[col] = le

# ========== 第四步：划分特征和标签 ==========
X = df_features.drop(columns=["pass"])
y = df_features["pass"]

# ========== 第五步：划分训练集和测试集 ==========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ========== 第六步：定义模型 ==========
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=0),
    "Decision Tree": DecisionTreeClassifier(random_state=0),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=0)
}

# ========== 第七步：训练与评估 ==========
for name, model in models.items():
    print(f"\n--- {name} ---")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# ========== 可选：保存模型 ==========
# from joblib import dump
# dump(model, 'random_forest_model.joblib')
