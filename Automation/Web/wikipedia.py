# import necessary packages
from selenium import webdriver
import pyttsx3 as p

# class to see the information
class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mtiwari33\Downloads\Softwares\chromedriver_win32\chromedriver")

    def get_info(self, query):
        """
        Takes query which is the text extracted from speech and then using that text it searches about the text and speaks the paragraph for wikipedia
        :param query: text -> extracted from speech
        """
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)

        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()

        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]')
        readable_text = info.text
        engine = p.init()
        try:
            engine.say(readable_text)
        except KeyboardInterrupt():
            print("Interrupted from keyboard")
        engine.runAndWait()

# # Testing
# bot = info()
# bot.get_info("Ram Mandir")

