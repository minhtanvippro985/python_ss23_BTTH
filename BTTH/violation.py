from datetime import datetime


def evaluate_flex_time(attendance_book):
    late_stamp = datetime.strptime("10:00", "%H:%M")
    for record in attendance_book:
        gio_vao_str, gio_ra_str = record["times"]
        if gio_ra_str is None:
            print(
                f"{record['id']} - {record['name']}: Đang làm việc"
            )
            continue
        time_in = datetime.strptime(gio_vao_str, "%H:%M")
        time_out = datetime.strptime(gio_ra_str, "%H:%M")
        if time_in > late_stamp:
            print(
                f"{record['id']} - Vi phạm: Đến muộn quá 90 phút ({gio_vao_str})."
            )
        else:
            duration = time_out - time_in
            total_hours = duration.total_seconds() / 3600
            if total_hours < 9.0:
                print(
                    f"{record['id']} -chưa hoàn thành đủ 9 tiếng bù giờ."
                )
            else:
                print(
                    f"{record['id']} - Hoàn thành ca làm việc."
                )
