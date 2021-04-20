from ctypes import windll
for i in range(10000):
    print(windll.user32.GetSystemMetrics(i))