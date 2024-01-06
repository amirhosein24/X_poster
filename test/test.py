from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def scrape_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find('span', class_='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3').text
    return text

def scrape_tweets(username, num_tweets=10):
    url = f'https://twitter.com/{username}'

    # Use the path to your webdriver executable
    driver_path = 'chromedriver.exe'  # Replace with the actual path to chromedriver

    # Use ChromeService to set executable path
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    print("opened")
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    print("sleep done")
    # Scroll down to load more tweets (you may need to adjust this loop)
    for _ in range(num_tweets // 2):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
    print("searching")

    # Get the HTML source of the page
    html = driver.page_source

    # Scrape the text from the HTML
    text = scrape_text_from_html(html)
    print(f'Text: {text}\n')

    print("for done")
    driver.quit()

if __name__ == "__main__":
    target_username = "garshaspx"
    num_tweets_to_scrape = 5
    scrape_tweets(target_username, num_tweets_to_scrape)