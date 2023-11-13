def choose_unit():
    while True:
        unit = input('Ban muon chuyen sang:\n Do C  hoac do F: ').lower()
        if unit == "c":
            return "c"
            break
        elif unit == "f":
            return "f"
            break
        else:
            print("nhap sai, vui long chon lai")
            continue


def inputTemp():
    while True:
        n = input('Nhập nhiệt độ: ')
        try:
            n = int(n)  # Chuyển đổi chuỗi nhập thành số nguyên
            return n  # Trả về nếu nhập đúng kiểu dữ liệu
        except ValueError:
            print('Nhập lại nhiệt độ. Đây không phải là một số nguyên.')


a = float(inputTemp())


def TemperatureConvert(a):
    while True:
        if choose_unit() == 'c':
            nhietdo = (a - 32) * (5 / 9)
            nhietdo = round(nhietdo, 2)
            print(f'Nhiet do f thanh: {nhietdo} do c')
            break
        else:
            nhietdo = (a * 9 / 5) + 32
            nhietdo = round(nhietdo, 2)
            print(f'Nhiet do c thanh: {nhietdo} do f')
            break

TemperatureConvert(a)
