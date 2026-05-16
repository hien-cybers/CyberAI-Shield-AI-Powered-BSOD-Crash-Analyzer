import pandas as pd
import os

def generate_mock_dataset():
    # Giả lập các dữ liệu đã được bóc tách từ nhiều file log khác nhau
    # Cột 'Label' chính là "đáp án" để dạy AI
    data = [
        {"Bugcheck_String": "0xA", "Faulting_Module": "ntoskrnl.exe", "Crash_Code": "IRQL_NOT_LESS_OR_EQUAL", "Label": "Lỗi Driver/Hệ điều hành"},
        {"Bugcheck_String": "0x1A", "Faulting_Module": "nt!MmAccessFault", "Crash_Code": "MEMORY_MANAGEMENT", "Label": "Lỗi Phần cứng (RAM)"},
        {"Bugcheck_String": "0x3B", "Faulting_Module": "win32k.sys", "Crash_Code": "SYSTEM_SERVICE_EXCEPTION", "Label": "Lỗi Driver Đồ họa"},
        {"Bugcheck_String": "0x50", "Faulting_Module": "srv2.sys", "Crash_Code": "PAGE_FAULT_IN_NONPAGED_AREA", "Label": "Lỗ hổng Mạng (Gợi ý: CVE-2020-0796)"},
        {"Bugcheck_String": "0xC0000005", "Faulting_Module": "http.sys", "Crash_Code": "ACCESS_VIOLATION", "Label": "Lỗ hổng Bảo mật (Gợi ý: CVE-2022-21907)"}
    ]
    
    df = pd.DataFrame(data)
    
    # Tạo đường dẫn lưu file vào thư mục data
    output_path = "../data/bsod_dataset.csv"
    
    # Lưu bảng thành file CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Đã tạo thành công bộ dữ liệu tại: {output_path}")
    print(df)

if __name__ == "__main__":
    generate_mock_dataset()