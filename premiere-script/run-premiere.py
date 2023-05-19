import os
import time
import pyautogui

premiere_pro_exe = r"C:\Program Files\Adobe\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe"
script_path = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\premiere-script\merge-videos.jsx"

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

