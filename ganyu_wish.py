import pyautogui
import time

spam_cycle = 0
ganyu_wish = 0
hutao_wish = 0

print("script starting soon")
time.sleep(float(2.5))

while spam_cycle < 35:
    for i in range(10):
        time.sleep(float(1.125))
        pyautogui.typewrite("*wish ganyu", interval = 0.0225)
        pyautogui.press("enter")
        ganyu_wish += 1
    print(f"Wished on Ganyu {ganyu_wish} times and Hu Tao {hutao_wish} times")
    time.sleep(float(0.5)), time.sleep(float(5 * 60))

    for i in range(10):
        time.sleep(float(1.125))
        pyautogui.typewrite("*wish hu tao", interval = 0.0225)
        pyautogui.press("enter")
        hutao_wish += 1
    print(f"Wished on Ganyu {ganyu_wish} times and Hu Tao {hutao_wish} times")

    if spam_cycle != 35:
        time.sleep(float(0.5)), time.sleep(float(5 * 60))
    else:
        time.sleep(float(0.25))
        continue

    spam_cycle += 1
print("script completed")
print(f"Wished on Ganyu a total of {ganyu_wish} times and Hu Tao {hutao_wish} times.")
exit()
