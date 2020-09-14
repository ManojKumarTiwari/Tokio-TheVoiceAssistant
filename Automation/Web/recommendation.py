# import necessary packages
from selenium import webdriver
import pyttsx3 as p

# class to see the information
class IMDBlatestBestMovies():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mtiwari33\Downloads\Softwares\chromedriver_win32\chromedriver")

    def recommend(self):
        """
        just recommends the latest best movies according to the ratings in IMDB
        """
        self.driver.get(url='https://www.imdb.com/chart/moviemeter/?ref_%22nv_mv_mpm%22')
        sortBy = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
        sortBy.click()


# # Testing
# bot = IMDBlatestBestMovies()
# bot.recommend()