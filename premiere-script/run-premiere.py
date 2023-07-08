import os
import time
import pyautogui
import json
import subprocess

premiere_pro_exe = r"C:\Program Files\Adobe\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe"
script_path = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\merge-videos.jsx"
script_name = 'merge-videos.jsx'
extendScript_tab  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\button-screenshots\extendscript-tab.png"
open_button  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\button-screenshots\open.png"
run_button  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\button-screenshots\run.png"
merge_videos_icon  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\button-screenshots\merge-videos-desktop-icon.png"

# Open Premiere Pro
os.startfile(premiere_pro_exe)
time.sleep(7)

# Navigate to the New Project option
pyautogui.hotkey('ctrl', 'alt', 'n')
time.sleep(1)
pyautogui.press('enter')  # confirm to create new project
time.sleep(1)
pyautogui.press('tab')  # tab over in the duplicate name menu
time.sleep(1)
pyautogui.press('enter')  # confirm to create
time.sleep(1)

# Open Extend Scipt window and run extend script
loc = pyautogui.locateCenterOnScreen(extendScript_tab)
pyautogui.moveTo(loc)
pyautogui.click()
time.sleep(1)
loc = pyautogui.locateCenterOnScreen(open_button)
pyautogui.moveTo(loc)
pyautogui.click()
time.sleep(1)
loc = pyautogui.locateCenterOnScreen(merge_videos_icon)
pyautogui.moveTo(loc)
pyautogui.click()
time.sleep(1)
pyautogui.hotkey('enter')
loc = pyautogui.locateCenterOnScreen(run_button)
pyautogui.moveTo(loc)
pyautogui.click()
time.sleep(1)