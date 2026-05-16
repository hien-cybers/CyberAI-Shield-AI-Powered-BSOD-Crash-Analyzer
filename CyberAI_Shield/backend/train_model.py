import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle
import os

def train_ai_model():
    print("1. Đang đọc dữ liệu từ file CSV...")
    data_path = "../data/bsod_dataset.csv"
    
    if not os.path.exists(data_path):
        print("Lỗi: Không tìm thấy file dữ liệu. Hãy chắc chắn bạn đã chạy create_dataset.py")
        return

    df = pd.read_csv(data_path)

    # Gộp các cột đặc trưng lại thành một chuỗi văn bản duy nhất để AI dễ học
    df['Combined_Text'] = df['Bugcheck_String'] + " " + df['Faulting_Module'] + " " + df['Crash_Code']
    
    X = df['Combined_Text'] # Đầu vào (Đề bài)
    y = df['Label']         # Đầu ra (Đáp án)

    print("2. Đang xây dựng Pipeline (TF-IDF + Random Forest)...")
    # Pipeline giúp tự động hóa việc biến chữ thành số rồi đưa vào thuật toán
    model_pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer()),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    print("3. Bắt đầu huấn luyện mô hình...")
    model_pipeline.fit(X, y)
    print("=> Huấn luyện thành công!")

    # Lưu "Bộ não" của AI ra một file vật lý để sau này Web có thể sử dụng lại
    model_dir = "../models"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model_path = f"{model_dir}/bsod_model.pkl"
    with open(model_path, 'wb') as f:
        pickle.dump(model_pipeline, f)
    
    print(f"4. Đã lưu mô hình tại: {model_path}")

if __name__ == "__main__":
    train_ai_model()