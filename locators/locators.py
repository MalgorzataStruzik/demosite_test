from selenium.webdriver.common.by import By

class AddData:

    select_option = (By.XPATH, "//*[@id='TitleId']/option[2]")
    initial_input = (By.ID, 'Initial')
    name_input = (By.ID, "FirstName")
    middleName_input = (By.ID, "MiddleName")
    radiobox_gender = (By.XPATH, "//input[@name='Female']")
    checkbox_lang_eng = (By.NAME, "english")
    checkbox_lang_hindi = (By.NAME, "Hindi")