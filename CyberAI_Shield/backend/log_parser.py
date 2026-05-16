import re
import pandas as pd
import os

def parse_bsod_log(file_path):
    """
    Hàm này đọc file log txt và trích xuất các thông tin quan trọng.
    """
    # Tạo một dictionary (từ điển) để lưu trữ dữ liệu rỗng ban đầu
    log_data = {
        "Bugcheck_String": None,
        "Faulting_Module": None,
        "Crash_Code": None
    }
    
    # Kiểm tra xem file có tồn tại không
    if not os.path.exists(file_path):
        print(f"Không tìm thấy file: {file_path}")
        return None

    # Mở và đọc file log
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # 1. Trích xuất BUGCHECK_STR
        bugcheck_match = re.search(r"BUGCHECK_STR:\s+(.*)", content)
        if bugcheck_match:
            log_data["Bugcheck_String"] = bugcheck_match.group(1).strip()
            
        # 2. Trích xuất FAULTING_MODULE
        module_match = re.search(r"FAULTING_MODULE:\s+([^\s]+)", content)
        if module_match:
            log_data["Faulting_Module"] = module_match.group(1).strip()
            
        # 3. Trích xuất CRASH_CODE
        crash_code_match = re.search(r"CRASH_CODE:\s+(.*)", content)
        if crash_code_match:
            log_data["Crash_Code"] = crash_code_match.group(1).strip()

    return log_data

# === PHẦN CHẠY THỬ ===
if __name__ == "__main__":
    # Đường dẫn trỏ tới file log mẫu trong thư mục data
    # Dùng đường dẫn tương đối từ thư mục backend lùi lại 1 cấp (..) rồi vào data
    sample_file = "../data/sample_bsod.txt"
    
    # Gọi hàm bóc tách
    extracted_info = parse_bsod_log(sample_file)
    
    if extracted_info:
        # Chuyển đổi dữ liệu (dictionary) thành Pandas DataFrame (dạng bảng)
        df = pd.DataFrame([extracted_info])
        
        print("=== DỮ LIỆU ĐÃ BÓC TÁCH THÀNH CÔNG ===")
        print(df)