def clock_in(list_here):
    print("\n--- CHẤM CÔNG VÀO ---")
    nv_id = input("Nhập mã nhân viên: ").strip()

    for record in list_here:
        if record["id"] == nv_id:
            print(f"Mã nhân viên {nv_id} đã tồn tại!")
            return

    name = input("Nhập tên nhân viên: ").strip()
    gio_vao = input("Nhập giờ vào (HH:MM): ").strip()
    new_record = {"id": nv_id, "name": name, "times": (gio_vao, None)}
    list_here.append(new_record)
    print(f"Đã ghi nhận {nv_id} chấm công vào lúc {gio_vao}!")


def clock_out(list_here):
    print("\n--- CHẤM CÔNG RA ---")
    nv_id = input("Nhập mã nhân viên cần chấm công ra: ").strip()
    for record in list_here:
        if record["id"] == nv_id:
            gio_ra = input("Nhập giờ ra (HH:MM): ").strip()
            gio_vao_cu = record["times"][0]
            record["times"] = (gio_vao_cu, gio_ra)

            print(f"Nhân viên {nv_id} đã chấm công ra lúc {gio_ra}!")
            return

    print(f"Không tìm thấy nhân viên có mã {nv_id}!")

