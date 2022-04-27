"""
# this is scrape method from duckduckgo, which is working well but has a downside of not working with google search result
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def duckduckgo_knowledge_scrape(question):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # &iax=about - expanded knowledge graph
    # driver.get('https://duckduckgo.com/?q=' + question + '&kl=us-en&ia=web&iax=about')

    driver.get('https://duckduckgo.com/?q=' + question + '&kl=us-en&ia=web')
    title = driver.find_element(By.CSS_SELECTOR, '.module__title__link').text

    description = driver.find_element(By.CSS_SELECTOR, '.js-about-item-abstr').text.strip()
    print(f"{title}\n{description}")

    return "" +description
    driver.quit()
"""

# Calling Google Knowledge Graph Search API
# Limitation: only allows up to 100,000 (one hundred thousand) read calls per day per project at no charge
# https://developers.google.com/knowledge-graph/reference/rest/v1/usage-limits

from __future__ import print_function
import json
import urllib.parse
import urllib.request
import webbrowser


def google_knowledge_scrape(question):
    # bug3: if say something before "tell me about"/"what is"/... , it will include in the search, which is not good
    api_key = 'AIzaSyBp5tvMhBgJkWFYE6zxsXQwp-_DKoDpnBI'  # Dat's API, please replace with other APIs if needed
    query = question
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    params = {
        'query': query,
        'limit': 1,
        'indent': True,
        'key': api_key,
    }
    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())

    for element in response['itemListElement']:
        try:
            return element['result']['detailedDescription']['articleBody']
        # if there is no detailedDescription tag, return null
        except Exception:
            print("No knowledge box found. Passing return.")
            return None


def google_search(command):
    # replace interrogative word for better accuracy search
    query = command.lower()
    if "tell" in command:
        query = query.replace("tell me about", "")
        query = query.replace("tell about", "")
        query = query.replace("tell me", "")
        query = query.replace("tell", "")
    if "what" in command:
        query = query.replace("what is", "")
        query = query.replace("what are", "")
    elif "who" in command:
        query = query.replace("who is", "")
        query = query.replace("who are", "")
        query = query.replace("who", "")
    elif "why" in command:
        query = query.replace("why are", "")
        query = query.replace("why is", "")
        query = query.replace("why", "")
    elif "when" in command:
        query = query.replace("when is", "")
        query = query.replace("when are", "")
        query = query.replace("when", "")
    elif "search" in command:
        query = query.replace("search on google", "")
        query = query.replace("on google", "")
        query = query.replace("search", "")

    print("final command: " + query)
    if query or query != "" or query != " ":
        quote = google_knowledge_scrape(query)
        if quote is None:
            result = 'Here is what i found of "' + command + '"'
            url = "https://www.google.com/search?q=" + command
            webbrowser.open_new_tab(url)
        else:
            result = quote
        return result
    else:
        return None
