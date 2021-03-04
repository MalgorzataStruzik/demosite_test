from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pages.add_data_page import AddDataPage


@pytest.mark.usefixtures("setup")
class TestAddData:

    def test_entering_data(self):
        add_data_page = AddDataPage(self.driver)
        add_data_page.open_page()
        add_data_page.add_data_on_website()
        add_data_page.add_name("MS", "Gosia", "Strus")
        add_data_page.add_rest()

        assert "wszystko gra"
