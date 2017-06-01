from pages import *
from setup import *
from locators import *


class TestSuite:

    @classmethod
    def setup_class(cls):
        """What happens BEFORE tests"""
        cls.driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get(Links.main_page)

    @classmethod
    def teardown_class(cls):
        """What happens AFTER tests"""
        cls.driver.quit()

    def test_control_vacancy_invite(self):
        p = ControlVacancyPage(self.driver)
        HeaderPage(self.driver).login("1", "123123/")
        p.click_by_text("Формирование кадрового состава")
        p.click_by_text("Проведение конкурса на замещение вакантной должности")
        p.scroll_to_top()
        p.click_by_text("Подбор")
        p.table_select_row(1, "Выбор первой вакансии")
        p.scroll_to_top()
        p.click_by_text("Добавить кандидата")
        p.table_select_row(1, "Выбор первого кандидата")
        p.scroll_to_top()
        p.click_by_text("Направить приглашение")
        p.click_by_text("Направить приглашение", 2)
        p.scroll_to_top()
        p.click_by_text("Подбор")
        p.scroll_to_top()
        p.click_by_text("Закрыть")
        p.table_select_row(2, "Выбор второй вакансии")
        p.click_by_text("Добавить кандидата")
        p.table_select_row(1, "Выбор кандидата")
        p.scroll_to_top()
        p.click_by_text("Направить приглашение")
        p.click_by_text("Направить приглашение", 2)

    def tes7t_control_vacancy_statuses(self):
        p = ControlVacancyPage(self.driver)
        HeaderPage(self.driver).login("l&m", "123123/")
        p.click_by_text("Вакансии на контроле")
        p.click_by_text("Фильтр")
        p.status_response("Направлено приглашение")
        p.click_by_text("Применить")
        p.table_select_row(1, "Выбор приглашения")
        p.click_by_text("Принять приглашение")
        p.click_by_text("Продолжить")
        assert "Ваш отклик успешно завершен." not in self.driver.page_source
        p.click_by_text("Назад")
        p.table_select_row(1, "Выбор приглашения")
        p.click_by_text("Отклонить приглашение")
        p.click_by_text("Фильтр")
        p.select2_clear(ControlVacancyLocators.status_response)
        p.status_response("Отклонил приглашение")
        p.click_by_text("Применить")
        p.wait_for_text_appear("Отклонил приглашение")
        p.click_by_text("Дата события")
        p.click_by_text("Дата события")
        assert p.is_date_vacancy(), "Проверка \"Отклонил приглашение\" не прошла"
        p.click_by_text("Фильтр")
        p.select2_clear(ControlVacancyLocators.status_response)
        p.status_response("Приглашен")
        p.click_by_text("Применить")
        p.wait_for_text_appear("Приглашен")
        p.click_by_text("Дата события")
        p.click_by_text("Дата события")
        assert p.is_date_vacancy(), "Проверка \"Приглашен\" не прошла"