from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

driver.get("https://www.bi.go.id/id/umkm/database/umkm-layak-dibiayai.aspx")

time.sleep(3)

select = Select(driver.find_element(By.ID, 'ctl00_ctl44_g_ff19d8f7_b269_446c_8cd9_bb5484328fa8_ctl00_DropDownListProvinsi'))
select.select_by_visible_text("Jawa Barat")

time.sleep(5)
click1 = driver.find_element(By.ID, "ctl00_ctl44_g_ff19d8f7_b269_446c_8cd9_bb5484328fa8_ctl00_ListViewSektor_ctrl11_LinkButtonSektor")
driver.execute_script("arguments[0].click()", click1)

select = Select(driver.find_element(By.NAME, 'ctl00$ctl44$g_ff19d8f7_b269_446c_8cd9_bb5484328fa8$ctl00$DropDownListKredit'))
select.select_by_visible_text("Semua")

time.sleep(3)

while True:
    time.sleep(2)
    parameter = driver.find_element(By.CLASS_NAME, 'next')
    matches = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr a')
    matches2 = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr td:nth-child(5)')
    for match in matches:
        print(match.text)

    for match2 in matches2:
        print(match2.text)



    if parameter.get_attribute('disabled') == 'true':
        print("Data Sudah mencapai akhir")
        break

    next = driver.find_element(By.CLASS_NAME, 'next')
    driver.execute_script("arguments[0].click()", next)





time.sleep(5)