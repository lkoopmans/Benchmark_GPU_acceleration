import psutil

tst = psutil.disk_partitions()

for i in psutil.disk_partitions():
    print(i)
