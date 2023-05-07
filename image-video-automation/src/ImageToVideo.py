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

class ImageToVideo(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(ImageToVideo, self).__init__(options=options)
        self.implicitly_wait(20)
        self.set_window_size(1920, 1080)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.teardown:
        self.quit()

    def getHomePage(self):
        self.get("https://convert.leiapix.com/")

    def closePopup(self):
        sleep(1)
        close_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@name='popup-close-button']",))) 
        close_button.click()

    def signIn(self, email, password):
        sleep(1)
        sign_in_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='signInLink']",))) 
        sign_in_button.click()

        sleep(1)
        email_field: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='authUsername']",))) 
        email_field.send_keys(email)

        sleep(1)
        email_field: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='password']",))) 
        email_field.send_keys(password)

        sleep(1)
        submit_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']",))) 
        submit_button.click()

    def uploadImage(self, imagePath):
        sleep(1)
        chooseFile = self.find_element(By.XPATH, '//input[@type="file"]')
        chooseFile.send_keys(imagePath)

    def inputVideoFile(self, videoPath):
        videoInput = self.find_element_by_xpath('//input[@type="file"]')
        videoInput.send_keys(videoPath)

    # def editVideo(self):

    def downloadVideo(self):
        sleep(1)
        share_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@ng-click='shareClickHandler()']",))) 
        share_button.click()

        sleep(1)
        mp4_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='share-buttons-container']/button[2]",))) 
        mp4_button.click()

        sleep(1)
        save_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='brand-button brand-button-fill']",))) 
        save_button.click()

        sleep(5)
        close_button: WebElement = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-center ng-scope']/div/div/button[1]",))) 
        close_button.click()

    def convertImage(
            self,
            imageFilePaths,
    ):
        email = "historyqueefs@gmail.com"
        password = "QueefAlert$$69"
        self.getHomePage()
        self.closePopup()
        self.signIn(email, password)
        for image in imageFilePaths:
            self.uploadImage(image)
            self.downloadVideo()
            sleep(1)
        print("done!")
        sleep(5)

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
