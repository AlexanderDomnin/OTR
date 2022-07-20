from .base_page import BasePage
from core.locators.main_page_locators import MainPageLocators
import allure
from selenium.webdriver.common.by import By
from core.api.base_api import BaseApi


class MainPage(BasePage, BaseApi):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    @allure.step('Проверка футера на главной странице сайта')
    def assure_footer_on_main_page(self):
        assert self.is_element_present(*MainPageLocators.FOOTER), "Footer is not presented"

    @allure.step('Проверка ссылок на главной странице через API')
    def assure_link_on_main_page_api(self, status_code: int):
        list_link = self._get_link_on_page()
        list_code = self.get_status_code_response(url=list_link)
        for index, code in enumerate(list_code):
            assert code == status_code, f'Status code not {status_code} on - {code} in {index} element'

    @allure.step('Проверка корректности открытия ссылок')
    def assure_url_direct_on_correct_page(self):
        list_link = self._get_link_on_page()
        for link in list_link:
            self._open_link(link)
            self.should_be_correct_url(link)

    def _open_link(self, link: str):
        with allure.step(f'Открыть ссылку {link}'):
            self.browser.get(link)

    @allure.step('Получить список ссылок из элементов "a"')
    def _get_link_on_page(self):
        list_link = self.browser.find_elements(By.TAG_NAME, 'a')
        link_attr = [element.get_attribute('href') for element in list_link]
        return link_attr
