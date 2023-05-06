import os, os.path
import logging
import re
from time import sleep

from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from src.SeleniumCommon import login_using_cookie_file

class UploadTiktok(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(UploadTiktok, self).__init__(options=options)
        self.implicitly_wait(20)
        self.set_window_size(1920, 1080)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.teardown:
        self.quit()

    def getTiktokHomePage(self):
        self.get("https://www.tiktok.com")

    def getTiktokCreatorPage(self):
        self.get("https://www.tiktok.com/@mssp_clips")

    def clickUploadButton(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/upload?lang=en']//span//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]"))).click()

    def inputVideoFile(self, videoPath):
        sleep(1)
        self.find_element_by_xpath("//input[@accept='video/*']").send_keys(videoPath)

    def inputCaption(self, caption):
        sleep(3)
        self.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']").send_keys(caption)

    def waitForProcessing(self):
        postButton: WebElement = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Post']")))
        # progress_label: WebElement = self.find_element_by_xpath("//div[@class='tiktok-progress-inner']")
        # current_progress = progress_label.get_attribute("textContent")
        while "disabled" in postButton.get_attribute("class"):
            # if self.find_element_by_xpath("//div[@class='tiktok-progress-inner']"):
            #     current_progress = progress_label.get_attribute("textContent")
            #     print(current_progress)
                sleep(1)
        sleep(3)

    def clickPostButton(self):
        postButton: WebElement = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Post']"))).click()
        # Wait for the dialog to disappear
        sleep(10)
        logging.info("Tiktok upload is complete")

    def confirm_logged_in(self) -> bool:
        try:
            WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tiktok-1igqi6u-DivProfileContainer efubjyv0']")))
            return True
        except TimeoutError:
            return False

    def handle_iframe_bullshit(self):
        self.switch_to.frame(0)

    def startUpload(
            self,
            epNumber: str,
            videoTitle: str,
            videoPath: bool,
    ):
        login_using_cookie_file(self, cookie_file="config/tiktokCookies.json")
        self.getTiktokHomePage()
        self.confirm_logged_in()
        self.getTiktokCreatorPage()
        self.file_detector = LocalFileDetector()
        self.clickUploadButton()
        self.handle_iframe_bullshit()
        self.inputVideoFile(videoPath)
        self.inputCaption(getCaption(videoTitle, epNumber))
        self.waitForProcessing()
        self.clickPostButton()

def getCaption(title, epNumber) -> str:
    return """{title} | ep {epNumber} #DawgTok #MSSP #MattAndShanesSecretPodcast #ShaneGillis #comedy #podcast #comedyPodcast #podcastClips""".format(epNumber = epNumber, title = title)
    # todo 150 char check