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

    def test_search_vacancy(self):
        HeaderPage(self.driver).login("1", "123123/")
        p = SeachVacancyPage(self.driver)
        p.click_by_text("Поиск вакансий")
        p.click_by_text("Фильтр")
        p.click_by_text("Очистить")
        p.type_source_vacancy("ФОИВ")
        p.name_source_vacancy("Федеральная служба по гидрометеорологии и мониторингу окружающей среды")
        p.name_vacant_position("Руководитель федеральной службы")
        p.type_vacancy("Вакансия для замещения вакантной должности")
        p.substitution_competition("Нет")
        p.profile_activity_organization("Другое")
        p.key_word("Руководитель")
        p.click_by_text("Общие сведения")
        p.category_job("Руководители")
        p.group_job("Высшая")
        p.subject_workplace("г. Москва")
        p.region_workplace("Центральный")
        p.salary_from("20000")
        p.salary_to("30000")
        p.business_trip("10% служебного времени")
        p.work_day("5-ти дневная с.н. с 09-00 до 18-00")
        p.type_service_contract("Неважно")
        p.normal_workday("Да")
        p.click_by_text("Прием документов")
        p.day_start_accept_document_from("29.08.2016")
        p.day_stop_accept_document_to("19.09.2016")
        p.click_by_text("Квалификационные требования")
        p.level_education("Высшее образование")
        p.service_experience("Не менее 6 лет")
        p.work_experience_speciality("Не менее 7 лет")
        p.click_by_text("Применить")
        p.click_by_text("Руководитель федеральной службы")
        sleep(5)
        assert "Профиль деятельности организации" in self.driver.page_source