# import necessary packages
from selenium import webdriver
import pyttsx3 as p

# class to see the information
class Movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mtiwari33\Downloads\Softwares\chromedriver_win32\chromedriver")

    def movie_review(self, name):
        """
        Takes query which is the text extracted from speech and then using that text it searches for movie reviews and then speaks the ratings
        :param name: text -> extracted from speech
        :return:
        """
        self.driver.get(url='https://www.google.com/')
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + ' movie reviews')
        submit = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        submit.click()

        info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()

# # Testing
# bot = Movie()
# bot.movie_review('Avengers')
