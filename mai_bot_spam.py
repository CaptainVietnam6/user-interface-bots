import pyautogui
import time

spam_cycle = 0

while spam_cycle <= 249:
    time.sleep(float(0.20))
    pyautogui.typewrite("mai mai", interval = 0.0225)
    pyautogui.press("enter")
    spam_cycle = spam_cycle + 1
    print(f"spam script number {spam_cycle} complete")
