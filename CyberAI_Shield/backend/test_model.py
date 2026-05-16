import pickle
import pandas as pd
import os

def test_prediction():
    print("1. Đang đánh thức AI...")
    model_path = "../models/bsod_model.pkl"
    
    if not os.path.exists(model_path):
        print("Không tìm thấy file model!")
        return

    # Tải "bộ não" đã lưu lên bộ nhớ
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # 2. Tạo một ca bệnh mới. 
    # Giả sử đây là một file log do hệ thống thu thập được khi một chiếc laptop bất ngờ bị crash do xung đột phần mềm/phần cứng.
    new_error = {
        "Bugcheck_String": "0x50", 
        "Faulting_Module": "ntoskrnl.exe", 
        "Crash_Code": "PAGE_FAULT_IN_NONPAGED_AREA"
    }
    
    # Chuẩn bị dữ liệu theo đúng "ngôn ngữ" mà AI đã học (gộp chuỗi)
    df_new = pd.DataFrame([new_error])
    df_new['Combined_Text'] = df_new['Bugcheck_String'] + " " + df_new['Faulting_Module'] + " " + df_new['Crash_Code']
    
    print("\n2. Đưa ca bệnh vào phân tích...")
    # Yêu cầu AI đưa ra chẩn đoán
    prediction = model.predict(df_new['Combined_Text'])
    
    print("\n=== KẾT QUẢ CHẨN ĐOÁN CỦA AI ===")
    print(f"Dữ liệu đầu vào : {new_error['Crash_Code']} (Mã: {new_error['Bugcheck_String']}, Module: {new_error['Faulting_Module']})")
    print(f"AI kết luận     : >> {prediction[0]} <<")
    print("=================================\n")

if __name__ == "__main__":
    test_prediction()