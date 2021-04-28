import AppKit
import pyautogui
import schedule
import time
from datetime import date

def screenshot(t):
    screenshot = pyautogui.screenshot()
    d1 = date.today().strftime("%d%m%Y")
    screenshot.save("../images/screenshot_" + d1 + ".png")
    # pyautogui.hotkey('f5') #Simulates F5 key press = page refresh
    # print("did it")
    return

schedule.every().day.at("00:00").do(screenshot,'It is 00:00')

while True:
    print(schedule.get_jobs())
    schedule.run_pending()
    time.sleep(1) # wait one second

