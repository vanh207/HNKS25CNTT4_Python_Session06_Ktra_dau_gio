# câu 1
price = float(input("nhập vào đơn giá của 1 sản phẩm: "))
qty = int(input("nhập số lượng mua: "))
total_amount = price*qty
if total_amount >= 1000000:
    total_amount*=0.1
print(f"Số tiền phải thanh toán là {total_amount}")

# câu 2
password ="123456"
qty_input = 0
while True:
    input_password = input("Nhập mật khẩu: ")
    if input_password ==password:
        print("đăng nhập thành công")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        qty_input +=1
    if qty_input == 3:
        print("Tài khoản đã bị khóa!")
        break

# câu 3
qty_product = 0
qty_box = 0
while True:
    input_product = int(input("nhập số lượng thùng hàng: "))
    if input_product == 0:
        print(f"Tổng số thùng hàng hợp lệ đã đếm: {qty_box}")
        print(f"Tổng số lượng sản phẩm thu được: {qty_product}")
        break
    elif input_product < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!" )
    else:
        qty_product+=input_product
        qty_box+=1
    

