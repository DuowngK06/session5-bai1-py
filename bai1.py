branch_count = int(input("Nhập số lượng chi nhánh: "))
if branch_count <= 0:
    print("Số lượng chi nhánh không hợp lệ")
else:
    month_count = 3
    revenues = [[0] * branch_count for i in range(month_count)]
    for month in range(month_count):
        print("\nTháng", month + 1)
        for branch in range(branch_count):
            revenue = int(input("Nhập doanh thu chi nhánh: "))
            if revenue < 0:
                print("Doanh thu không hợp lệ")
                revenue = 0
            revenues[month][branch] = revenue
    print("\n===== BÁO CÁO DOANH THU =====")
    for month in range(month_count):
        print("\nTháng", month + 1)
        total = 0
        for branch in range(branch_count):
            print(
                "Chi nhánh",
                branch + 1,
                ":",
                revenues[month][branch],
                "triệu đồng"
            )
            total = total + revenues[month][branch]
        average = total / branch_count
        print("Tổng doanh thu:", total, "triệu đồng")
        print("Doanh thu trung bình:", average, "triệu đồng")
