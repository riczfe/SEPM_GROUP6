from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def duckduckgo_scrape_knowledge(question):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # &iax=about - expanded knowledge graph
    # driver.get('https://duckduckgo.com/?q=' + question + '&kl=us-en&ia=web&iax=about')

    driver.get('https://duckduckgo.com/?q=' + question + '&kl=us-en&ia=web')
    title = driver.find_element(By.CSS_SELECTOR, '.module__title__link').text

    description = driver.find_element(By.CSS_SELECTOR, '.js-about-item-abstr').text.strip()
    print(f"{title}\n{description}")

    return "" +description
    driver.quit()