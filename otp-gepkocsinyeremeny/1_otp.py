from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.otpbank.hu/portal/hu/Megtakaritas/ForintBetetek/Gepkocsinyeremeny")

raw_num = []

elem = browser.find_element_by_css_selector("#main > div > div > div > div > div:nth-child(9) > div > section > ul > li:nth-child(1)").get_attribute("innerHTML")
raw_num.append(elem[0:10])

elem = browser.find_element_by_css_selector("#main > div > div > div > div > div:nth-child(9) > div > section > ul > li:nth-child(2)").get_attribute("innerHTML")
raw_num.append(elem[0:10])

elem = browser.find_element_by_css_selector("#main > div > div > div > div > div:nth-child(9) > div > section > ul > li:nth-child(3)").get_attribute("innerHTML")
raw_num.append(elem[0:10])

elem = browser.find_element_by_css_selector("#main > div > div > div > div > div:nth-child(9) > div > section > ul > li:nth-child(4)").get_attribute("innerHTML")
raw_num.append(elem[0:10])

elem = browser.find_element_by_css_selector("#main > div > div > div > div > div:nth-child(9) > div > section > ul > li:nth-child(5)").get_attribute("innerHTML")
raw_num.append(elem[0:10])

for i in range(len(raw_num)):
    print(raw_num[i])

with open("uj_szamok_new.txt", "w") as uj_szamok:
    for i in range(len(raw_num)):
        uj_szamok.write(raw_num[i] + "\n")
