# webdriver inicializálása és a weboldal megnyitása

from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"
driver.get(URL)

# az operandusok és az operátor beolvasása, a művelet elvégzése és kiértékelése
num1 = int(driver.find_element_by_id("num1").text)
num2 = int(driver.find_element_by_id("num2").text)
operation = driver.find_element_by_id("op").text
driver.find_element_by_id("submit").click()
expected_result = int(driver.find_element_by_id("result").text)
actual_result = int(eval(f'{num1}{operation}{num2}'))

assert expected_result == actual_result
driver.close()
