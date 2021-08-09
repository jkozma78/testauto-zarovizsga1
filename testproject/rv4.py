# webdriver inicializálása és a weboldal megnyitása

from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"
driver.get(URL)


# search differece between two list
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


# az összes várost tartalmazó lista
all_cities = (driver.find_element_by_id("cites").text).split(', ')

# a felsorolásban megjelenő városok és azok listába rendezése
citi_list = []
actual_cities = driver.find_elements_by_tag_name("li")
for i in actual_cities:
    citi_list.append((f'"{i.text}"'))

# hiányzó város kikeresése
missing_citi = (str(Diff(citi_list, all_cities))[3:-3])

# a találat ellenőrzése
driver.find_element_by_id("missingCity").send_keys(missing_citi)
driver.find_element_by_id("submit").click()
actual = driver.find_element_by_id("result").text
result = ("Eltaláltad.")
assert actual == result

driver.close()
