from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigate to web page
driver.get("https://www.reddit.com/")

# locate search box
search = driver.find_element(By.NAME, "q")

# enter search term
search.send_keys("puppies")
search.send_keys(Keys.RETURN)

try:
    # locate search results
    search_results = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, r"QBfRw7Rj8UkxybFpX-USO"))
    )

    # scrape post headings
    posts = search_results.find_elements(By.CSS_SELECTOR, r"h3._eYtD2XCVieq6emjKBH3m")

    for post in posts:
        print(post.text)
finally:
    # quit browser
    driver.quit()
