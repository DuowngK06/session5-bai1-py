branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
revenues = []
for month in range(1, month_count + 1):
    month_data = []

    for branch in range(1, branch_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        month_data.append(revenue)

    revenues.append(month_data)
print("\n===== BÁO CÁO DOANH THU =====")
for month in range(1, month_count + 1):
    print(f"\nTháng {month}:")
    for branch in range(1, branch_count + 1):
        print(
            f"Chi nhánh {branch}, tháng {month}: "
            f"{revenues[month - 1][branch - 1]} triệu đồng"
        )