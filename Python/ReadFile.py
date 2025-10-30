# Mở file ở chế độ 'w' để ghi (warning: mode 'w' sẽ xóa hết nội dung cũ)
with open("/home/nghiavu/PycharmProjects/PythonProject/Document/Document.txt", "a") as f:
    f.write("Now the file has more content!")

# Đọc nội dung file sau khi ghi
with open("/home/nghiavu/PycharmProjects/PythonProject/Document/Document.txt", "r") as f:
    print(f.read())