from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service as ChromeService

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

    # Find and print tweets
    tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweet"]')

    for i, tweet in enumerate(tweets[:num_tweets]):
        print(i, tweet)
        try:
            # Some tweets may not have text or have different structures, handle exceptions
            tweet_text = tweet.find_element(By.XPATH, './/div[@lang="en"]').text
            print(f'Tweet {i + 1}: {tweet_text}\n')
        except Exception as e:
            print(f'Error processing tweet {i + 1}: {str(e)}\n')
    print("for done")
    driver.quit()

if __name__ == "__main__":
    target_username = "garshaspx"
    num_tweets_to_scrape = 5
    scrape_tweets(target_username, num_tweets_to_scrape)