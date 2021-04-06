import pyautogui
import time

spam_cycle = 0

while spam_cycle <= 24:
    spam_script = input("What script do you want to use to spam people with?: ")
    time.sleep(3)
    f = open(spam_script, "r")
    for word in f:
        time.sleep(float(0.20))
        pyautogui.typewrite("@everyone ")
        pyautogui.typewrite(word, interval = 0.0225)
        pyautogui.press("enter")
    spam_cycle = spam_cycle + 1
    print(f"spam script number {spam_cycle} complete")
