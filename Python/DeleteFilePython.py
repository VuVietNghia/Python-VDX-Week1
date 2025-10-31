import os
if os.path.exists("/home/nghiavu/Desktop/Document.txt"):
  os.remove("/home/nghiavu/Desktop/Document.txt")
else:
  print("The file does not exist")