import pyautogui
import time 

count = int(input("Sayiyi Belirtin: "))

message = input("Gidecek olan mesaji yazin: ")

time.sleep(5)

while(count > 0):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")

    count -= 1

print("Sonlandi")