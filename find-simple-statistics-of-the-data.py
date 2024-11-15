import pandas as pd
import statistics

def calculate_statistics(file_path):
    # อ่านไฟล์ CSV
    data = pd.read_csv(file_path)
    # print(data)

    # คำนวณสถิติพื้นฐาน
    min_val = data.min()
    max_val = data.max()
    total_sum = data.sum()
    mean = data.mean()
    
    # คำนวณส่วนเบี่ยงเบนมาตรฐาน (Standard Deviation)
    std_dev = data.std()

    # แสดงผลลัพธ์
    print("Minimum values:\n", min_val)
    print("\nMaximum values:\n", max_val)
    print("\nSum of each column:\n", total_sum)
    print("\nMean values:\n", mean)
    print("\nStandard Deviation:\n", std_dev)

# ทดสอบโปรแกรม
file_path = 'assignment1.2.csv'  # เปลี่ยนเป็นชื่อไฟล์ CSV ที่ต้องการอ่าน
calculate_statistics(file_path)
