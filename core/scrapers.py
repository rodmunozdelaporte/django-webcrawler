from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .models import NewsItem



def scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument(' - incognito')

    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

    browser.get(url)

    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@class='crayons-story__body']")
            )
        )
    except TimeoutException:
        print("Timeout waiting for page to load")
        browser.quit()
    

    article_elements = browser.find_elements_by_xpath("//div[@class='crayons-story__body']")

    for article in article_elements:
        parent = article.find_element_by_css_selector(".crayons-story__title")
        result = parent.find_element(By.TAG_NAME, "a")
        print(result.text)
        print(result.get_attribute('href'))

        # Search for time
        news_item_time = article.find_element_by_tag_name('time')
        
        NewsItem.objects.get_or_create(
            titulo=result.text,
            fuente='Dev.to',
            link=result.get_attribute('href')
        )

