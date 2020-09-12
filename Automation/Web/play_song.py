# import necessary packages
from selenium import webdriver

# class to see the information
class Music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mtiwari33\Downloads\Softwares\chromedriver_win32\chromedriver")

    def fromytvideo(self, name):
        """
        Takes query which is the text extracted from speech and then using that text it searches in Youtube and plays it
        :param name: text -> extracted from speech
        :return:
        """
        self.name = name
        self.driver.get(url='https://www.youtube.com/results?search_query=' + name)
        video = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        video.click()

# # Test
# bot = Music()
# bot.fromytvideo('in the end')



