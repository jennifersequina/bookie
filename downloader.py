from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def downloader(user_input):

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()

    print("Chromedriver installed and maximized")

    book_title = user_input
    driver.get("http://www.oceanofpdf.com")

    print("Ocean of PDF webpage opened")

    search_bar = driver.find_element(By.ID, "searchform-1")
    search_bar.send_keys(book_title)
    search_bar.send_keys(Keys.RETURN)

    print("Book title searched")

    result = driver.find_element(By.CLASS_NAME, "entry-title-link")
    result.click()

    print("Search result clicked")

    epub = driver.find_element(By.XPATH, "//div//input[@alt='Submit' and @src='https://oceanofpdf.com/wp-content/uploads/epub-button.jpg']")
    epub.send_keys()
    epub.click()

    print("EPUB clicked for download")

    time.sleep(15)
    driver.close()
    driver.quit()

    print("EPUB is now ready for processing")

