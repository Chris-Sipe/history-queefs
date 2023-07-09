import os
import time
import pyautogui

class RunPremiere:

    def run(self):

        script_file = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\merge-videos"
        premiere_pro_exe = r"C:\Program Files\Adobe\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe"
        extendScript_tab  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\extendscript-tab.png"
        extendScript_tab2  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\extendscript-tab2.png"
        open_button  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\open.png"
        run_button  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\run.png"
        merge_videos_icon  = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\merge-videos-desktop-icon.png"
        home_button = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\home.png"
        premiere_script_button = r"C:\Users\chris\OneDrive\Documents\history-queefs\history-queefs\PremiereScript\button-screenshots\premiere-script.png"

        # Open Premiere Pro
        os.startfile(premiere_pro_exe)
        time.sleep(10)

        # Navigate to the New Project option
        pyautogui.hotkey('ctrl', 'alt', 'n')
        time.sleep(1)
        pyautogui.press('enter')  # confirm to create new project
        time.sleep(1)
        pyautogui.press('tab')  # tab over in the duplicate name menu
        time.sleep(1)
        pyautogui.press('enter')  # confirm to create
        time.sleep(3)

        # Open Extend Scipt window and run extend script
        self.click(extendScript_tab)
        print("1")
        self.click(extendScript_tab2)
        print("2")
        self.click(open_button)
        print("3")
        self.click(home_button)
        print("4")
        self.click(premiere_script_button)
        pyautogui.hotkey('enter')
        time.sleep(1)
        self.click(merge_videos_icon)
        pyautogui.hotkey('enter')
        time.sleep(1)
        self.click(run_button)

    def click(self, button):
        loc = pyautogui.locateCenterOnScreen(button)
        pyautogui.moveTo(loc)
        pyautogui.click()
        time.sleep(1)