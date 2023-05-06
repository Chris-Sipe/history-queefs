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

class UploadYoutube(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(UploadYoutube, self).__init__(options=options)
        self.implicitly_wait(20)
        self.set_window_size(1920, 1080)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.teardown:
        self.quit()

    def getYoutubeHomePage(self):
        self.get("https://www.youtube.com")

    def getYoutubeStudioPage(self):
        self.get("https://studio.youtube.com")

    def clickCreateButton(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytcp-button#create-icon"))).click()

    def clickUploadButton(self):
        WebDriverWait(self, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//tp-yt-paper-item[@test-id="upload-beta"]'))).click()

    def inputVideoFile(self, videoPath):
        videoInput = self.find_element_by_xpath('//input[@type="file"]')
        videoInput.send_keys(videoPath)

    def inputTitle(self, title):
        titleInput: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,'//ytcp-social-suggestions-textbox[@id="title-textarea"]//div[@id="textbox"]',))) 
        titleInput.clear()
        titleInput.send_keys(title)

    def inputDescription(self, description):
        descriptionInput: WebElement = self.find_element_by_xpath('//ytcp-social-suggestions-textbox[@id="description-textarea"]//div[@id="textbox"]')
        descriptionInput.send_keys(description)

    def inputNotMadeForKids(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK"))).click()

    def inputVisibility(self):
        for i in range(3):
            WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.ID, "next-button"))).click()
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-radio-button[@name='PUBLIC']//div[@id='offRadio']"))).click()

    def waitForProcessing(self):
        progress_label: WebElement = self.find_element_by_css_selector("span.progress-label")
        pattern = re.compile(r"(finished processing)|(processing hd.*)|(check.*)")
        current_progress = progress_label.get_attribute("textContent")
        last_progress = None
        while not pattern.match(current_progress.lower()):
            if last_progress != current_progress:
                logging.info(f'Current progress: {current_progress}')
            last_progress = current_progress
            sleep(5)
            current_progress = progress_label.get_attribute("textContent")

    def clickPublishButton(self):
        self.find_element_by_css_selector("#step-badge-1").click()

        for _ in range(2):
            # Sometimes, the button is clickable but clicking it raises an error, so we add a "safety-sleep" here
            sleep(5)
            WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.ID, "next-button"))).click()

        sleep(5)
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Publish']"))).click()

        # Wait for the dialog to disappear
        sleep(5)
        logging.info("Youtube upload is complete")

    def confirm_logged_in(driver: WebDriver) -> bool:
        """ Confirm that the user is logged in. The browser needs to be navigated to a YouTube page. """
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "avatar-btn")))
            return True
        except TimeoutError:
            return False


    def startUpload(
            self,
            epNumber: str,
            epTitle: str,
            epYoutubeLink: str,
            videoTitle: str,
            videoPath: bool,
    ):
        login_using_cookie_file(self, cookie_file="config/youtubeCookies.json")
        self.getHomePage()
        self.confirm_logged_in()
        self.clickUploadButton()
        self.file_detector = LocalFileDetector()
        self.inputVideoFile(videoPath)
        
        # self.getYoutubeStudioPage()
        # self.file_detector = LocalFileDetector()
        # self.clickCreateButton()
        # self.clickUploadButton()
        # self.inputVideoFile(videoPath)
        # self.inputTitle(videoTitle)
        # self.inputDescription(getDescription(epNumber, epTitle, epYoutubeLink))
        # self.inputNotMadeForKids()
        # self.inputVisibility()
        # self.waitForProcessing()
        # self.clickPublishButton()

def getDescription(number, title, youtubeLink) -> str:
        return """MSSP Podcast: https://bit.ly/3ubmaU9
Ep {epNumber} - {EpTitle}: {EpYoutubeLink}
•
Unofficial Clips Channel:
Tik Tok: https://bit.ly/3wpfQv6
Instagram: https://bit.ly/3wv9cTM
Youtube: https://bit.ly/3KZpXKV
Linktree: https://bit.ly/3D1nuNw
•
#MSSP #dawgs #MattAndShanesSecretPodcast #ShaneGillis  #comedy #podcast #comedyPodcast #podcastClips #shorts""".format(epNumber = number, EpTitle = title, EpYoutubeLink = youtubeLink)
