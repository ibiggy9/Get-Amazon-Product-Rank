from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from openpyxl import load_workbook

class Scrape:
    def __init__(self, url):
        self.PATH = "/Users/main/desktop/code/scraping/chromedriver_PATH_for_selenium_ref/chromedriver"
        self.chrome_options = Options()
        self.chrome_options.headless = True
        self.chrome_options.add_argument = ("--disable-extensions")
        self.chrome_options.add_argument = ("--disable-gpu")
        self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)
        self.actions = ActionChains(self.driver)
        self.url = url
        self.product_name = []
 
        self.zipped_list = []
        self.rating_list = []
     
  
        try:
            self.get_info()
        finally:
            pass
            self.return_data()
    

        
    

    def get_info(self):
        self.driver.get(self.url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        try:
            product_name = self.driver.find_element_by_css_selector("#productTitle").text
            rating = self.soup.find('span',{'id':'acrPopover', 'title':True})
            self.product_name.append(product_name)
            self.rating_list.append(rating.get('title').strip())

        except:
            print('Failed')
            pass
 
        

        self.zipped_list = list(zip(self.product_name, self.rating_list))
        print(self.zipped_list)

        self.driver.close()
    
    

    def return_data(self):
        
        wb = load_workbook('data.xlsx')
        ws = wb.active
        for i in self.zipped_list:
            ws.append(i)
        
        wb.save('data.xlsx')
        



    
        