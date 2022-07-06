from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button(driver):
    driver.get(link)
    time.sleep(5)
    get_button = driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    get_button_text = get_button.text
    print(get_button_text)
    assert 'Añadir al carrito' == get_button_text