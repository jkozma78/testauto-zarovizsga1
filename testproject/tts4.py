# webdriver inicializálása és a weboldal megnyitása

from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
driver.get(URL)
# számláló a "fej" számolásásra
count_head = 0
# megnyomjuk 100x a "pémzfeldobás" gombot
for _ in range(100):
    driver.find_element_by_id("submit").click()
    # ha a "lastResult" textje fej, akkor növeljük eggyel a számlálót
    if driver.find_element_by_id("lastResult").text == "fej":
        count_head = count_head + 1

assert count_head >= 30
driver.close()
