# webdriver inicializálása és a weboldal megnyitása

from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"
driver.get(URL)

testdata = {"99": ("12", "222"), "kiskutya": ("12", "NaN"), "": ("", "NaN")}


# függvény a testadatok bevitelére és az adatok ellenőrzésére
def cases(a, b, expected_result):
    driver.find_element_by_id("a").clear()
    driver.find_element_by_id("a").send_keys(a)
    driver.find_element_by_id("b").clear()
    driver.find_element_by_id("b").send_keys(b)
    driver.find_element_by_id("submit").click()
    actual_result = driver.find_element_by_id("result").text
    assert actual_result == expected_result


# cases függvény meghívása tesztadatokkal
for x in testdata:
    cases(x, testdata[x][0], testdata[x][1])

driver.close()
