from selenium import webdriver
import time
from fake_useragent import UserAgent


class Parsing():
	def __init__(self):
		self.useragent = UserAgent()

		# self.option = webdriver.ChromeOptions()
		# self.option.add_argument(f"user-agent={self.useragent.random}")
		# self.browser = webdriver.Chrome(executable_path=r'C:\Users\Andrey\Desktop\Projects\KP_test\chrome_driver\chromedriver.exe', chrome_options=self.option)

		self.option = webdriver.FirefoxOptions()
		# self.option.set_preference("general.useragent.override", f"{self.useragent.random}")
		self.option.set_preference('dom.webdriver.enabled', False)
		self.browser = webdriver.Firefox(executable_path=r'C:\Users\Andrey\Desktop\Projects\KP_test\firefox_driver\geckodriver.exe', options=self.option)

		self.browser.get('https://www.kinopoisk.ru/')
		time.sleep(0.5)
	def parse(self, title_film):
		genre_mass = []
		time.sleep(1)
		input_tab = self.browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/header/div/div[2]/div[2]/div/form/div/input')
		time.sleep(0.2)
		input_tab.send_keys(f"{title_film}")
		time.sleep(1.5)
		input_film = self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/header/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/article/a').click()
		time.sleep(2)
		title = self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/h1/span').text
		genre = self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div').text
		g = self.browser.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div/a')
		for i in g:
			genre_mass.append(i.text)
		# print(genre_mass)
		# test = self.browser.find_element('//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div')

		time.sleep(2)
		self.browser.quit()

		return title, genre, genre_mass

# if __name__ == "__main__":
# 	connector = Parsing()
# 	connector.parse()