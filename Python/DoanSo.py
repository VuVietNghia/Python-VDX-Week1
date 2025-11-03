import random

canDuoi = int(input("Nhap can duoi: "))
canTren = int(input("Nhap can tren: "))
soRandom = random.randint(canDuoi, canTren)

while True:
    soDoan = int(input("Nhap so doan: "))

    if soDoan < soRandom:
        print("So doan nho hon")
    elif soDoan > soRandom:
        print("So doan lon hon")
    else:
        print("Chuc mung ban da doan dung")
        is_running = False
