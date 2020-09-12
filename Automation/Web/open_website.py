# import necessary packages
from selenium import webdriver
import pyttsx3 as p

# class to see the information
class Website():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mtiwari33\Downloads\Softwares\chromedriver_win32\chromedriver")

    def open_website(self, website_name):
        """
        Takes query which is the text extracted from speech and then using that text it searches about the text and speaks the paragraph for wikipedia
        :param query: text -> extracted from speech
        """
        self.website_name = website_name
        self.driver.get(url="https://" + website_name)

# # Testing
# bot = Website()
# bot.open_website("facebook.com")