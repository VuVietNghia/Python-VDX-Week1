def mayTinh():
    so1_input = input("Nhap so a: ")
    so1 = float(so1_input)

    so2_input = input("Nhap so b: ")
    so2 = float(so2_input)

    phepTinh = input("Nhap phep tinh(+ - * /): ")
    so3 = None

    if phepTinh == '+':
        so3 = so1 + so2
    elif phepTinh == '-':
        so3 = so1 - so2
    elif phepTinh == '*':
        so3 = so1 * so2
    elif phepTinh == '/':
        if so2 == 0:
            print("Khong the chia het cho 0")
            return
        else:
            so3 = so1 / so2
    print(f"{so1} {phepTinh} {so2} = {so3}")
mayTinh()