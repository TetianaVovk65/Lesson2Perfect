from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

FULL_NAME_FIELD = '//input[@id="userName"]'
EMAIL_FIELD = '//input[@id="userEmail"]'
CUR_ADDR_FIELD = '//textarea[@id="currentAddress"]'
PERM_ADDR_FIELD = '//textarea[@id="permanentAddress"]'
SUBMIT_BUTTON = '//button[@id="submit"]'
EMAIL_ERROR = '//input[@id="email"][contains(@class),"error"]'


def test_text_boxes1(chrome):
    driver = chrome
    driver.get('https://demoqa.com/text-box')
    name = driver.find_element(By.XPATH, FULL_NAME_FIELD)
    email = driver.find_element(By.XPATH, EMAIL_FIELD)
    current_address = driver.find_element(By.XPATH, CUR_ADDR_FIELD)
    permanent_address = driver.find_element(By.XPATH, PERM_ADDR_FIELD)
    submit = driver.find_element(By.XPATH, SUBMIT_BUTTON)

    name.send_keys('VOVK Tetiana')
    email.send_keys('mail@mail.com')
    current_address.send_keys('Shevchenka str.')
    permanent_address.send_keys('Heroiv UPA')
    driver.execute_script("arguments[0].scrollIntoView()", submit)
    submit.click()

    name_val = name.get_attribute('value')
    email_val = email.get_attribute('value')
    current_address_val = current_address.get_attribute('value')
    permanent_address_val = permanent_address.get_attribute('value')

    result_name = driver.find_element(By.ID, 'name').text.split(':')[1]
    result_email = driver.find_element(By.ID, 'email').text.split(':')[1]
    result_current_address = driver.find_element(By.CSS_SELECTOR, 'p[id=currentAddress]').text.split(':')[1]
    result_permanent_address = driver.find_element(By.CSS_SELECTOR, 'p[id=permanentAddress]').text.split(':')[1]

    control_data = [name_val == result_name,
                    email_val == result_email,
                    current_address_val == result_current_address,
                    permanent_address_val == result_permanent_address]
    assert all(control_data)


def test_invalid_email(chrome):
    driver = chrome
    driver.get('https://demoqa.com/text-box')

    email = driver.find_element(By.XPATH, EMAIL_FIELD)
    submit = driver.find_element(By.XPATH, SUBMIT_BUTTON)
    email.send_keys('mail@@mail,com')

    driver.execute_script("arguments[0].scrollIntoView()", submit)
    submit.click()

    assert email == driver.find_element(By.XPATH, EMAIL_ERROR)# як перевірити що поле емейл містить клас з словом еррор?
