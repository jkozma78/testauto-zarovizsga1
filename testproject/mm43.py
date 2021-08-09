# webdriver inicializálása és a weboldal megnyitása

from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"
driver.get(URL)

testdata = {"teszt@elek.hu": "", "teszt@": "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.",
            "": "Kérjük, töltse ki ezt a mezőt."}


def email_validation(email, epexcted):
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("submit").click()
    if len(driver.find_elements_by_xpath('//div[@class="validation-error"]')) < 1:
        actual_result = ""
    else:
        actual_result = driver.find_element_by_xpath('//div[@class="validation-error"]').text
    assert actual_result == epexcted


for i in testdata:
    email_validation(i, testdata[i])

driver.close()
