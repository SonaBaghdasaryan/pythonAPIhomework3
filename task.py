# Задание
# Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной
# странице личного кабинета. Должно проверятся открытие формы, ввод данных в поля, клик по
# кнопке и появление всплывающего alert.
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text
# Формат сдачи: В качестве решения принимается написанный нами ранее проект с добавлением
# шага по проверке Contact Us и правками всех необходимых вспомогательных файлов.


import yaml
from pagetest import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pswd"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAILED"


def test_contact_us(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pswd"])
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.add_name(testdata["u_name"])
    testpage.add_email(testdata["u_email"])
    testpage.add_contact_content(testdata["content_contact"])
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test contact us FAILED!"