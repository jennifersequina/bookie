from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")


book_title = "Atomic Habits"
driver.get("https://www.oceanofpdf.com")

search_bar = driver.find_element(By.ID, "searchform-1")
search_bar.send_keys(book_title)
search_bar.send_keys(Keys.RETURN)

result = driver.find_element(By.CLASS_NAME, "entry-title-link")
result.click()

epub = driver.find_element(By.XPATH, "//div//input[@alt='Submit' and @src='https://oceanofpdf.com/wp-content/uploads/epub-button.jpg']")
epub.send_keys()
epub.click()
