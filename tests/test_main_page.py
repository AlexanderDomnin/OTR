import allure
from core.data.url import Url
from pages.main_page import MainPage


@allure.suite('Тесты главной страницы')
class TestMainPage:

    @allure.feature('Проверка главной страницы mos.ru')
    def test_mosru(self, browser):
        with allure.step('Шаг 1: Перейти на страницу https://www.mos.ru/'):
            main_page = MainPage(browser, url=Url.MAIN_SCREEN)
            main_page.open()
        with allure.step('Шаг 2: Проверить наличие шапки подвала'):
            main_page.assure_footer_on_main_page()
        with allure.step('Шаг 3: Проверить все ссылки со страницы и проверить их на 200'):
            main_page.assure_link_on_main_page_api(status_code=200)
        with allure.step('Шаг 4: Открыть каждую ссылку и проверить адресную строку браузера,'
                         ' что открывается нужная ссылка'):
            main_page.assure_url_direct_on_correct_page()
