import time
from selenium import webdriver
import math

data = {
    "link": "http://suninjuly.github.io/math.html"
}


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def execute_task():
    browser = webdriver.Chrome()
    try:
        browser.get(data['link'])
        x_value = browser.find_element_by_id('input_value').text

        input_result = browser.find_element_by_id('answer')

        input_result.send_keys(calc(x_value))

        robot_option = browser.find_element_by_id('robotCheckbox')
        robot_option.click()

        robot_rule_option = browser.find_element_by_css_selector("[for = 'robotsRule']")
        robot_rule_option.click()

        send_button = browser.find_element_by_css_selector('button.btn')
        send_button.click()

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    execute_task()