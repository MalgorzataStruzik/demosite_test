from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demosite.executeautomation.com/index.html")
checkbox_lang_eng = driver.find_element(By.NAME, "english")
if checkbox_lang_eng.get_attribute("checked") == "true":
    checkbox_lang_eng.click()