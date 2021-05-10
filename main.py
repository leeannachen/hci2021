import AppKit
import pyautogui
import schedule
import time
from datetime import date

# from https://pyautogui.readthedocs.io/en/latest/screenshot.html
def screenshot(t):
    screenshot = pyautogui.screenshot()
    d1 = date.today().strftime("%d%m%Y")
    screenshot.save("images/"+ "screenshot_" + d1 + ".png")
    return

schedule.every().day.at("00:00").do(screenshot,'It is 00:00')

while True:
    print(schedule.get_jobs())
    schedule.run_pending()
    time.sleep(1) # wait one second

