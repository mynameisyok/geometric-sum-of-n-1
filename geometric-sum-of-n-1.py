from fractions import Fraction

def geometric_series_sum(a1, r, n):
    # ตรวจสอบว่า r ไม่เท่ากับ 1
    if r == 1:
        # return "Error: r must not be equal to 1."
        return "r equal to 1 so the answer is a1: " + str(a1)
    
    # เปลี่ยนค่า n ให้เป็น n-1
    n = n - 1

    # คำนวณผลรวมอนุกรมเรขาคณิตตามสูตร
    Sn = a1 * (r**n - 1) / (r - 1)
    return Sn

while 1:
    # รับค่าจากผู้ใช้
    a1 = float(Fraction(input("Enter the first term (a1): ")))
    n = int(input("Enter the number of terms (n): "))
    r = float(Fraction(input("Enter the common ratio (r): ")))

    # แสดงผลลัพธ์
    result = geometric_series_sum(a1, r, n)

    if (r == 1):
        print(result)
    else:
        print("The sum of the geometric series of n-1 is:", result)
