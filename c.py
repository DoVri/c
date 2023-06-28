import os

ip_target = input("Masukkan IP target: ")
os.system(f"shutdown /s /t 120 /m \\\\{ip_target}")
