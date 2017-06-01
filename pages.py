from locators import *
from framework import *
from setup import *


parent = Browser


class HeaderPage(parent):

    def username(self, value):
        self.set_text(HeaderLocators.username, value, "Username")

    def password(self, value):
        self.set_text(HeaderLocators.password, value, "Password")

    def submit(self):
        self.click(HeaderLocators.submit, "submit")

    def login(self, username, password):
        self.driver.get(Links.main_page)
        if "Войти" in self.driver.page_source:
            self.click_by_text("Войти")
            try:
                self.click_by_text("Войти", 2)
            except EC.NoSuchElementException:
                pass
            self.username(username)
            self.password(password)
            self.submit()
            self.wait_for_text_appear("Личные данные")
        else:
            self.scroll_to_top()
            self.logout()
            self.login(username, password)

    def logout(self):
        self.driver.get(Links.main_page)
        self.wait_for_loading()
        self.scroll_to_top()
        self.click((By.XPATH, "//input[@type='submit']"))

    def dashboard(self):
        self.click(HeaderLocators.dashboard, "На главную")


class OrdersPage(parent):

    def submit(self, full_name, order, date, by, position):
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_select_row()
        self.click_by_text("Включить в приказ")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[3]"), position, "Должность подписанта")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[2]"), by, "ФИО подписанта")
        self.set_date((By.XPATH, "(//input[@type='text'])[2]"), date, "Дата приказа")
        self.set_text((By.XPATH, "(//input[@type='text'])[1]"), order, "Номер приказа")
        self.set_select2((By.XPATH, "(//div[contains(@id, 's2id')])[3]"), position, "Должность подписанта")
        self.click((By.XPATH, "//input[@value='Сохранить']"), "Сохранить")
        self.wait_for_text_appear("Приказ успешно утвержден.")
        self.click((By.XPATH, "//small[.='3']"), "Исполнение приказов ")
        self.click_by_text("Фильтр")
        self.set_text((By.XPATH, "//input[@type='text']"), full_name, "Фамилия Имя Отчество")
        self.click_by_text("Применить")
        self.table_select_row()
        self.click_by_text("Завершить")


class SeachVacancyPage(parent):

    def type_source_vacancy(self, value):
        self.set_select2_alt(SearchVacancyLocators.type_source_vacancy, value, "Тип источника вакансии")

    def name_source_vacancy(self, value):
        self.set_text(SearchVacancyLocators.name_source_vacancy, value, "Наименование источника вакансии")

    def name_vacant_position(self, value):
        self.set_text(SearchVacancyLocators.name_vacant_position, value, "Наименование вакантной должности")

    def type_vacancy(self, value):
        self.set_select2_alt(SearchVacancyLocators.type_vacancy, value, "Тип вакансии")

    def substitution_competition(self, value):
        self.set_select(value, 1, "Замещение по конкурсу")

    def profile_activity_organization(self, value):
        self.set_select2_alt(SearchVacancyLocators.profile_activity_organization,
                             value, "Профиль деятельности организации")

    def field_professional_activity(self, value):
        self.set_select2_alt(SearchVacancyLocators.field_professional_activity,
                             value, "Область профессиональной деятельности")

    def key_word(self, value):
        self.set_text(SearchVacancyLocators.key_word, value, "Ключевое слово")

    def category_job(self, value):
        self.set_select2_alt(SearchVacancyLocators.category_job, value, "Категория должности")

    def group_job(self, value):
        self.set_select2_alt(SearchVacancyLocators.group_job, value, "Группа должности")

    def subject_workplace(self, value):
        self.set_select2(SearchVacancyLocators.subject_workplace, value, "Расположение рабочего места (субъект)")

    def region_workplace(self, value):
        self.set_select2(SearchVacancyLocators.region_workplace, value, "Расположение рабочего места (регион)")

    def salary_from(self, value):
        self.set_text(SearchVacancyLocators.salary_from, value, "Размер оплаты труда от")

    def salary_to(self, value):
        self.set_text(SearchVacancyLocators.salary_to, value, "Размер оплаты труда до")

    def business_trip(self, value):
        self.set_select2(SearchVacancyLocators.business_trip, value, "Командировки")

    def work_day(self, value):
        self.set_select2(SearchVacancyLocators.work_day, value, "Рабочий день")

    def type_service_contract(self, value):
        self.set_select(value, 2, "Тип служебного контракта (трудового договора)")

    def normal_workday(self, value):
        self.set_select(value, 3, "Нормированный рабочий день")

    def day_start_accept_document_from(self, value):
        self.set_date(SearchVacancyLocators.day_start_accept_document_from, value, "Дата начала приема документов с")

    def day_start_accept_document_to(self, value):
        self.set_date(SearchVacancyLocators.day_start_accept_document_to, value, "Дата начала приема документов по")

    def day_stop_accept_document_from(self, value):
        self.set_date(SearchVacancyLocators.day_stop_accept_document_from, value, "Дата окончания приема документов с")

    def day_stop_accept_document_to(self, value):
        self.set_date(SearchVacancyLocators.day_stop_accept_document_to, value, "Дата окончания приема документов по")

    def level_education(self, value):
        self.set_select2_alt(SearchVacancyLocators.level_education, value, "Уровень образования")

    def service_experience(self, value):
        self.set_select2_alt(SearchVacancyLocators.service_experience, value, "Стаж государственной службы")

    def work_experience_speciality(self, value):
        self.set_select2_alt(SearchVacancyLocators.work_experience_speciality, value, "Опыт работы по специальности")


class ControlVacancyPage(parent):

    @property
    def subcontrol(self):
        return self.SubControl(self.driver)

    def checkbox_selection_vacancy_second(self):
        self.table_select_row("Выбрана вакансия вторая")

    def status_response(self, value):
        self.set_select2_alt(ControlVacancyLocators.status_response, value, "Статус отклика")

    def is_date_vacancy(self):
        self.wait_for_loading()
        elements = self.driver.find_elements_by_xpath("//tr[@class='ng-scope']//td[7]")
        texts = []
        for i in elements:
            texts.append(i.text.split()[0])
        return str(datetime.date.today().day) in texts

    class SubControl(parent):

        def status(self, value):
            self.set_select2_alt(ControlVacancyLocators.status_response, value, "Статус")


class DocumentsPage(parent):

    def has_appform (self):
        self.driver.get(Links.appform)
        self.wait_for_loading()
        if "Анкета 667" in self.driver.page_source:
            self.click_by_text("Анкета 667")
            self.wait_for_loading()
        else:
            self.click_by_text("Добавить")
            self.wait_for_text_appear("Загрузить")

    def name_document(self, value):
        self.set_select2(DocumentsLocators.name_document, value, "Название")

    def selection_radio(self):
        self.click(DocumentsLocators.selection_radio, "Выбор анкеты")

    def lastname_667_r(self, value):
        self.set_text(DocumentsLocators.lastname_667_r, value, "Фамилия")

    def firstname_667_r(self, value):
        self.set_text(DocumentsLocators.firstname_667_r, value, "Имя")

    def middlename_667_r(self, value):
        self.set_text(DocumentsLocators.middlename_667_r, value, "Отчество")

    def gender_667_r(self, value):
        self.set_select2(DocumentsLocators.gender_667_r, value, "Пол")

    def individual_taxpayer_number_667_r(self, value):
        self.set_text(DocumentsLocators.individual_taxpayer_number_667_r, value, "СНИЛС")

    def insurance_certificate_number_667_r(self, value):
        self.set_text(DocumentsLocators.insurance_certificate_number_667_r, value, "СНИЛС")

    def birthdate_667_r(self, value):
        self.set_date(DocumentsLocators.birthdate_667_r, value, "Дата рождения")

    def citizenship_667_r(self, value):
        self.set_select2(DocumentsLocators.citizenship_667_r, value, "Гражданство")

    def change_citizenship_667_r(self, value):
        self.set_select(value, 1, "Изменение гражданства")

    def birthplace_667_r(self, value):
        self.set_text(DocumentsLocators.birthplace_667_r, value, "Место рождения")

    def wasconvicted_667_r(self, value):
        self.set_select(value, 2, "Наличие судимостей")

    def maritalstatuses_667_r(self, value):
        self.set_select2(DocumentsLocators.maritalstatuses_667_r, value, "Семейное положение")

    def namewaschanged_667_r(self, value):
        self.set_select(value, 3, "Сведения об изменении ФИО")

    def wasabroad_667_r(self, value):
        self.set_select(value, 4, "Пребывание за границей")

    def work_phone_667_r(self, value):
        self.set_text(DocumentsLocators.work_phone_667_r, value, "Рабочий телефон")

    def mobile_phone_667_r(self, value):
        self.set_text(DocumentsLocators.mobile_phone_667_r, value, "Мобильный телефон")

    def additional_phone_667_r(self, value):
        self.set_text(DocumentsLocators.additional_phone_667_r, value, "Дополнительный телефон")

    def fax_667_r(self, value):
        self.set_text(DocumentsLocators.fax_667_r, value, "Факс")

    def work_email_667_r(self, value):
        self.set_text(DocumentsLocators.work_email_667_r, value, "Рабочая электронная почта")

    def personal_email_667_r(self, value):
        self.set_text(DocumentsLocators.personal_email_667_r, value, "Персональная электронная почта")

    def web_address_667_r(self, value):
        self.set_text(DocumentsLocators.web_address_667_r, value, "Персональная интернет-страница")

    def permanent_registration_sub_667_r(self, value):
        self.set_select2(
            DocumentsLocators.permanent_registration_sub_667_r, value, "Постоянная регистрация - субъект")

    def permanent_registration_reg_667_r(self, value):
        self.set_select2(
            DocumentsLocators.permanent_registration_reg_667_r, value, "Постоянная регистрация - регион")

    def temp_registration_sub_667_r(self, value):
        self.set_select2(
            DocumentsLocators.temp_registration_sub_667_r, value, "Временная регистрация - субъект")

    def temp_registration_reg_667_r(self, value):
        self.set_select2(
            DocumentsLocators.temp_registration_reg_667_r, value, "Временная регистрация - регион")

    def fact_registration_sub_667_r(self, value):
        self.set_select2(
            DocumentsLocators.fact_registration_sub_667_r, value, "Фактическое проживание - субъект")

    def fact_registration_reg_667_r(self, value):
        self.set_select2(
            DocumentsLocators.fact_registration_reg_667_r, value, "Фактическое проживание - регион")

    def type_document_667_r(self, value):
        self.set_select2(
            DocumentsLocators.type_document_667_r, value, "Тип документа")

    def series_667_r(self, value):
        self.set_text(DocumentsLocators.series_667_r, value, "Серия")

    def number_667_r(self, value):
        self.set_text(DocumentsLocators.number_667_r, value, "Номер")

    def date_issued_667_r(self, value):
        self.set_date(DocumentsLocators.date_issued_667_r, value, "Дата выдачи")

    def date_end_667_r(self, value):
        self.set_date(DocumentsLocators.date_end_667_r, value, "Дата окончания действия")

    def issue_by_667_r(self, value):
        self.set_text(DocumentsLocators.issue_by_667_r, value, "Кем выдан")

    def issue_code_667_r(self, value):
        self.set_text(DocumentsLocators.issue_code_667_r, value, "Код подразделения")

    def education_level_667_r(self, value):
        self.set_select2(DocumentsLocators.education_level_667_r, value, "Образовательный уровень")

    def education_667_r(self, value):
        self.set_select2(DocumentsLocators.education_667_r, value, "Образование")

    def education_form_667_r(self, value):
        self.set_select2(DocumentsLocators.education_form_667_r, value, "Форма обучения")

    def place_institution_667_r(self, value):
        self.set_text(DocumentsLocators.place_institution_667_r, value, "Расположение учебного заведения")

    def full_name_institution_667_r(self, value):
        self.set_select2(
            DocumentsLocators.full_name_institution_667_r, value, "Полное название учебного заведения")

    def start_date_education_667_r(self, value):
        self.set_text(DocumentsLocators.start_date_education_667_r, value, "Год начала")

    def end_date_education_667_r(self, value):
        self.set_text(DocumentsLocators.end_date_education_667_r, value, "Год окончания")

    def education_directions_667_r(self, value):
        self.set_select2(
            DocumentsLocators.education_directions_667_r, value, "Направление образования (форма 1ГС)")

    def faculty_667_r(self, value):
        self.set_text(DocumentsLocators.faculty_667_r, value, "Факультет")

    def education_doc_number_667_r(self, value):
        self.set_text(DocumentsLocators.education_doc_number_667_r, value, "Номер диплома")

    def education_doc_date_667_r(self, value):
        self.set_date(DocumentsLocators.education_doc_date_667_r, value, "Дата выдачи диплома")

    def speciality_667_r(self, value):
        self.set_select2(
            DocumentsLocators.speciality_667_r, value, "Специальность / направление подготовки по диплому")

    def qualification_667_r(self, value):
        self.set_select2(DocumentsLocators.qualification_667_r, value, "Квалификация по диплому")

    def specialization_667_r(self, value):
        self.set_text(DocumentsLocators.specialization_667_r, value, "Специализация по диплому")

    def is_main_667_r(self, value):
        self.set_checkbox(DocumentsLocators.is_main_667_r, value, "Основное")

    def egc_education_667_r(self, value):
        self.set_select2(
            DocumentsLocators.egc_education_667_r, value, "Послевузовское профессиональное образование")

    def egc_place_667_r(self, value):
        self.set_text(DocumentsLocators.egc_place_667_r, value, "Расположение учебного заведения")

    def egc_name_institution_667_r(self, value):
        self.set_text(
            DocumentsLocators.egc_name_institution_667_r, value, "Название учебного заведения")

    def egc_start_date_667_r(self, value):
        self.set_text(DocumentsLocators.egc_start_date_667_r, value, "Год начала")

    def egc_end_date_667_r(self, value):
        self.set_text(DocumentsLocators.egc_end_date_667_r, value, "Год окончания")

    def egc_academic_degree_667_r(self, value):
        self.set_select2(DocumentsLocators.egc_academic_degree_667_r, value, "Ученая степень")

    def egc_academic_degree_date_667_r(self, value):
        self.set_date_enter(
            DocumentsLocators.egc_academic_degree_date_667_r, value, "Дата присвоения ученой степени")

    def egc_knowledge_branches_667_r(self, value):
        self.set_select2(DocumentsLocators.egc_knowledge_branches_667_r, value, "Отрасль наук")

    def egc_diplom_number_667_r(self, value):
        self.set_text(DocumentsLocators.egc_diplom_number_667_r, value, "Номер диплома")

    def egc_diplom_date_667_r(self, value):
        self.set_date_enter(DocumentsLocators.egc_diplom_date_667_r, value, "Дата выдачи диплома")

    def academic_statuses_667_r(self, value):
        self.set_select2(DocumentsLocators.academic_statuses_667_r, value, "Учёное звание")

    def diplom_number_667_r(self, value):
        self.set_text(DocumentsLocators.diplom_number_667_r, value, "Номер аттестата")

    def assigment_date_667_r(self, value):
        self.set_date_enter(DocumentsLocators.assigment_date_667_r, value, "Дата присвоения ученого звания")

    def languages_667_r(self, value):
        self.set_select2(DocumentsLocators.languages_667_r, value, "Язык")

    def language_degrees_667_r(self, value):
        self.set_select2(DocumentsLocators.language_degrees_667_r, value, "Уровень владения")

    def dpo_education_direction_667_r(self, value):
        self.set_select2(DocumentsLocators.dpo_education_direction_667_r, value, "Направление подготовки")

    def dpo_education_kind_667_r(self, value):
        self.set_select2(DocumentsLocators.dpo_education_kind_667_r, value, "Вид образовательной программы")

    def dpo_kind_667_r(self, value):
        self.set_text(DocumentsLocators.dpo_kind_667_r, value, "Вид повышения квалификации")

    def dpo_name_program_667_r(self, value):
        self.set_text(DocumentsLocators.dpo_name_program_667_r, value, "Название программы")

    def dpo_education_form_667_r(self, value):
        self.set_select2(DocumentsLocators.dpo_education_form_667_r, value, "Форма обучения")

    def dpo_place_667_r(self, value):
        self.set_text(DocumentsLocators.dpo_place_667_r, value, "Расположение учебного заведения")

    def dpo_name_institution_667_r(self, value):
        self.set_text(DocumentsLocators.dpo_name_institution_667_r, value, "Наименование учебного заведения")

    def dpo_start_date_667_r(self, value):
        self.set_select2(DocumentsLocators.dpo_start_date_667_r, value, "Год начала")

    def dpo_end_date_667_r(self, value):
        self.set_select2(DocumentsLocators.dpo_end_date_667_r, value, "Год окончания")

    def dpo_hours_667_r(self, value):
        self.set_text(DocumentsLocators.dpo_hours_667_r, value, "Количество часов")

    def dpo_document_number_667_r(self, value):
        self.set_text(
            DocumentsLocators.dpo_document_number_667_r, value, "Документ о ДПО (наименование, номер)")

    def dpo_document_date_667_r(self, value):
        self.set_date_enter(DocumentsLocators.dpo_document_date_667_r, value, "Дата документа о ДПО")

    def dpo_funding_sources_667_r(self, value):
        self.set_select2(DocumentsLocators.dpo_funding_sources_667_r, value, "Источник финансирования")

    def work_begin_date_667_r(self, value):
        self.set_date(DocumentsLocators.work_begin_date_667_r, value, "Начало деятельности")

    def work_end_date_667_r(self, value):
        self.set_date(DocumentsLocators.work_end_date_667_r, value, "Окончание деятельности")

    def work_post_667_r(self, value):
        self.set_text(DocumentsLocators.work_post_667_r, value, "Должность")

    def work_organization_667_r(self, value):
        self.set_text(DocumentsLocators.work_organization_667_r, value, "Организация")

    def work_address_organization_667_r(self, value):
        self.set_text(DocumentsLocators.work_address_organization_667_r, value, "Адрес организации")

    def work_employees_number_667_r(self, value):
        self.set_select2(DocumentsLocators.work_employees_number_667_r, value, "Количество сотрудников")

    def work_subject_667_r(self, value):
        self.set_select2(DocumentsLocators.work_subject_667_r, value, "Субъект расположения организации")

    def work_region_667_r(self, value):
        self.set_select2(DocumentsLocators.work_region_667_r, value, "Регион расположения организации")

    def work_profile_667_r(self, value):
        self.set_select2(DocumentsLocators.work_profile_667_r, value, "Профиль деятельности организации")

    def work_is_elective_667_r(self, value):
        self.move_to_element(self.find((By.XPATH, "//button[.='Сохранить']")))
        self.set_checkbox(DocumentsLocators.work_is_elective_667_r, value, "Выборная должность")

    def work_post_level_667_r(self, value):
        self.set_select2(DocumentsLocators.work_post_level_667_r, value, "Уровень должности")

    def work_activity_area_667_r(self, value):
        self.set_select2(
            DocumentsLocators.work_activity_area_667_r, value, "Область профессиональной деятельности")

    def work_structural_division_667_r(self, value):
        self.set_text(DocumentsLocators.work_structural_division_667_r, value, "Подразделение")

    def work_responsibilities_667_r(self, value):
        self.set_text(DocumentsLocators.work_responsibilities_667_r, value, "Функции/обязанности")

    def has_class_rank_667_r(self, value):
        self.set_checkbox(DocumentsLocators.has_class_rank_667_r, value, "Имеется ли классный чин")

    def class_rank_667_r(self, value):
        self.set_text(DocumentsLocators.class_rank_667_r, value, "Классный чин")

    def class_rank_assigned_date_667_r(self, value):
        self.set_date_enter(DocumentsLocators.class_rank_assigned_date_667_r, value, "Когда присвоен")

    def class_rank_assigned_by_667_r(self, value):
        self.set_text(DocumentsLocators.class_rank_assigned_by_667_r, value, "Кем присвоен")

    def has_government_service_667_r(self, value):
        self.set_checkbox(
            DocumentsLocators.has_government_service_667_r, value, "Государственная или муниципальная служба")

    def org_sub_types_667_r(self, value):
        self.set_select2(DocumentsLocators.org_sub_types_667_r, value, "Направление")

    def organization_name_667_r(self, value):
        self.set_text(DocumentsLocators.organization_name_667_r, value, "Организация")

    def computer_skills_667_r(self, value):
        self.set_text(DocumentsLocators.computer_skills_667_r, value, "Владение персональным компьютером")

    def publications_667_r(self, value):
        self.set_text(DocumentsLocators.publications_667_r, value, "Публикации")

    def recommendations_667_r(self, value):
        self.set_text(DocumentsLocators.recommendations_667_r, value, "Рекомендации")

    def specialization_work_667_r(self, value):
        self.set_select2(DocumentsLocators.specialization_work_667_r, value, "Специализация")

    def specialization_is_main_667_r(self, value):
        self.set_checkbox(DocumentsLocators.specialization_is_main_667_r, value, "Основная")

    def specialization_is_add_667_r(self, value):
        self.set_checkbox(DocumentsLocators.specialization_is_add_667_r, value, "Дополнительная")

    def award_type_667_r(self, value):
        self.set_select2(DocumentsLocators.award_type_667_r, value, "Вид")

    def award_name_667_r(self, value):
        self.set_text(DocumentsLocators.award_name_667_r, value, "Наименование")

    def award_date_667_r(self, value):
        self.set_text(DocumentsLocators.award_date_667_r, value, "Дата")

    def admission_form_667_r(self, value):
        self.set_select2(DocumentsLocators.admission_form_667_r, value, "Форма допуска")

    def approval_number_667_r(self, value):
        self.set_text(DocumentsLocators.approval_number_667_r, value, "Номер допуска")

    def issue_date_667_r(self, value):
        self.set_date_enter(DocumentsLocators.issue_date_667_r, value, "Дата")

    def military_rank_667_r(self, value):
        self.set_select2(DocumentsLocators.military_rank_667_r, value, "Воинское звание")

    def military_duty_667_r(self, value):
        self.set_select2(DocumentsLocators.military_duty_667_r, value, "Воинская обязанность")

    def has_military_service_667_r(self, value):
        self.set_checkbox(
            DocumentsLocators.has_military_service_667_r, value, "Проходили ли срочную военную службу?")

    def military_service_from_667_r(self, value):
        self.set_date_tab(DocumentsLocators.military_service_from_667_r, value, "Начало службы")

    def military_service_to_667_r(self, value):
        self.set_date_enter(DocumentsLocators.military_service_to_667_r, value, "Род войск")

    def arm_kind_667_r(self, value):
        self.set_text(DocumentsLocators.arm_kind_667_r, value, "Окончание службы")

    def kin_ship_667_r(self, value):
        self.set_select2(DocumentsLocators.kin_ship_667_r, value, "Степень родства")

    def kin_last_name_667_r(self, value):
        self.set_text(DocumentsLocators.kin_last_name_667_r, value, "Фамилия")

    def kin_first_name_667_r(self, value):
        self.set_text(DocumentsLocators.kin_first_name_667_r, value, "Имя")

    def kin_middle_name_667_r(self, value):
        self.set_text(DocumentsLocators.kin_middle_name_667_r, value, "Отчество")

    def kin_name_changes_667_r(self, value):
        self.set_text(
            DocumentsLocators.kin_name_changes_667_r, value, "Изменения ФИО (старое значение, дата, причина)")

    def kin_birth_country_667_r(self, value):
        self.set_select2(DocumentsLocators.kin_birth_country_667_r, value, "Место рождения (страна)")

    def kin_birth_region_667_r(self, value):
        self.set_select2(DocumentsLocators.kin_birth_region_667_r, value, "Место рождения (субъект)")

    def kin_birth_area_667_r(self, value):
        self.set_select2(DocumentsLocators.kin_birth_area_667_r, value, "Место рождения (район)")

    def kin_birth_place_667_r(self, value):
        self.set_text(DocumentsLocators.kin_birth_place_667_r, value, "Место рождения")

    def kin_work_place_667_r(self, value):
        self.set_text(DocumentsLocators.kin_work_place_667_r, value, "Место работы (наим. и ад. орг.), должность")

    def kin_living_country_667_r(self, value):
        self.set_select2(
            DocumentsLocators.kin_living_country_667_r, value, "Cтрана проживания")

    def kin_living_address_667_r(self, value):
        self.set_text(DocumentsLocators.kin_living_address_667_r, value, "Домашний адрес")

    def kin_birth_date_667_r(self, value):
        self.set_date_enter(DocumentsLocators.kin_birth_date_667_r, value, "Дата рождения")
