from locators import locators


class AddDataPage:

    def __init__(self, driver):
        self.driver = driver
        #data elements
        self.select_option = locators.AddData.select_option
        self.initial_input = locators.AddData.initial_input
        self.name_input = locators.AddData.name_input
        self.middleName_input = locators.AddData.middleName_input
        self.radiobox_gender = locators.AddData.radiobox_gender
        self.checkbox_lang_eng = locators.AddData.checkbox_lang_eng
        self.checkbox_lang_hindi = locators.AddData.checkbox_lang_hindi
        self.displayed_details = locators.AddData.displayed_details

    def open_page(self):
        self.driver.get("https://demosite.executeautomation.com/index.html")

    def add_data_on_website(self):
        self.driver.find_element(*self.select_option).click()

    def add_name(self,initial,name, middleName):
        self.driver.find_element(*self.initial_input).send_keys(initial)
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.middleName_input).send_keys(middleName)

    def add_rest(self):
        self.driver.find_element(*self.radiobox_gender).click()
        self.driver.find_element(*self.checkbox_lang_eng).click()
        #if self.checkbox_lang_eng.get_attribute("checked") == "true":
         #   self.checkbox_lang_eng.click()
        self.driver.find_element(*self.checkbox_lang_hindi).click()