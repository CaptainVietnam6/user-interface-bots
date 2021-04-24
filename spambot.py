'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#7932
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: ACTIVE, FINALISED
'''

import pyautogui
import time

spam_cycle = 0

while spam_cycle <= 24:
    spam_script = input("enter script you want to use to spam people with: ")
    time.sleep(3)
    f = open(spam_script, "r")
    for word in f:
        time.sleep(float(0.20))
        pyautogui.typewrite("@everyone ")
        pyautogui.typewrite(word, interval = 0.0225)
        pyautogui.press("enter")
    spam_cycle = spam_cycle + 1
    print(f"spam script number {spam_cycle} complete")
