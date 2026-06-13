import tabulate


def display_records(list_here):
    headers = ["Mã NV", "Tên Nhân Viên", "Giờ Vào", "Giờ Ra"]
    formatted_data = []

    for record in list_here:
        gio_vao, gio_ra = record["times"]
        if gio_ra is None:
            gio_ra = "[Đang làm việc]"
        formatted_data.append([record["id"], record["name"], gio_vao, gio_ra])

    print(tabulate(formatted_data, headers=headers, tablefmt="simple"))