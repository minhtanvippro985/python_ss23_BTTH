import data 
import ui_display
import violation
import attendance_logic


while True:
    choice = input("""
=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===
1. Xem bảng chấm công ngày
2. Chấm công Vào (Clock-in)
3. Chấm công Ra (Clock-out)
4. Đánh giá vi phạm
5. Thoát chương trình 
================================================= 
Chọn chức năng (1-5): 
""")
    match choice:
        case "1":
            ui_display.display_records(data.attendance_book)
        case "2":
            attendance_logic.clock_in(data.attendance_book)
        case "3":
            attendance_logic.clock_out(data.attendance_book)
        case "4":
            violation.evaluate_flex_time(data.attendance_book)
        case "5":
            print("Thoát chương trình,...")
            break
        case _:
            print("Vui lòng chọn 1 - 5")