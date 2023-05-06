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

class UploadInstagram(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_extension("/Users/chrissipe/Development/clips-uploader/config/bcocdbombenodlegijagbhdjbifpiijp.crx")
        super(UploadInstagram, self).__init__(options=options)
        self.implicitly_wait(20)
        self.set_window_size(1920, 1080)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.teardown:
        self.quit()

    def getInstagramHomePage(self):
        self.get("https://www.instagram.com/")

    def getInstagramStudioPage(self):
        self.get("https://www.instagram.com/mssp_clips/")

    def clickPlusButton(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='wpO6b ZQScA ']//div[@class='QBdPU ']//*[name()='svg']"))).click()
        
    def clickCreateReelButton(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-id='reel']"))).click()

    def clickSelectFileButton(self, videoPath):
        self.find_element_by_xpath("//input[@accept='video/mp4,video/quicktime']").send_keys(videoPath)

    def clickNextButton(self):
        sleep(2)
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    def inputCaption(self, caption):
        self.find_element_by_xpath("//textarea[contains(@placeholder,'Write a caption...')]").send_keys(caption)

    def clickShareToFeedSwitch(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ShareToFeed__switch']"))).click()

    def clickShareButton(self):
        WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Share']"))).click()
        # Wait for the dialog to disappear
        sleep(20)

    def waitForProcessing(self):
        sleep(5) # TODO figure out proper waiting time

    def clickFirstPic(self):
        posts = []
        links = self.find_elements_by_tag_name("a")
        for link in links:
            post = link.get_attribute("href")
            if "/p/" in post:
                posts.append(post)
        self.get(posts[0])

    def addComment(self, comment):
        commentInput: WebElement = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Add a comment…']"))).click()
        WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Add a comment…']"))).send_keys(comment)
   
    def postComment(self):
        postComment: WebElement = WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Post']"))).click()
        sleep(5)
        logging.info("Instagram upload is complete")

    def confirm_logged_in(self) -> bool:
        try:
            WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='wpO6b ZQScA ']")))
            return True
        except TimeoutError:
            return False

    def startUpload(
            self,
            epNumber: str,
            videoTitle: str,
            videoPath: bool,
    ):
        self.getInstagramHomePage()
        login_using_cookie_file(self, cookie_file="config/instagramCookies.json")        
        # self.confirm_logged_in()
        self.getInstagramStudioPage()
        self.file_detector = LocalFileDetector()
        self.clickPlusButton()
        self.clickCreateReelButton()
        self.clickSelectFileButton(videoPath)
        self.clickNextButton()
        self.clickNextButton()
        sleep(2)
        self.waitForProcessing()
        sleep(2)
        self.clickShareToFeedSwitch()
        sleep(2)
        self.inputCaption(getCaption(videoTitle, epNumber))
        sleep(8)
        self.clickShareButton()
        sleep(2)
        self.getInstagramStudioPage()
        self.clickFirstPic()
        self.addComment(getComment())
        self.postComment()
        

def getCaption(title, epNumber) -> str:
        return """{title} | ep {epNumber}""".format(epNumber = epNumber, title = title)

def getComment() -> str:
    return """#MSSP #MattAndShanesSecretPodcast #dawgs #ShaneGillis #MattMcCusker #comedy #podcast #comedyPodcast #podcastClips #podcastClip #comedyReels #podcastReels #reels"""