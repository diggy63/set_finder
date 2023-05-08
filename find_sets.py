from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas


# create a new instance of the Firefox driver
driver = webdriver.Firefox()

# navigate to the page
driver.get("https://www.cardkingdom.com/catalog/search?search=mtg_advanced&filter%5Bsort%5D=name&filter%5Bsearch%5D=mtg_advanced&filter%5Btab%5D=mtg_card&filter%5Bname%5D=&filter%5Bedition%5D=3rd-edition&filter%5Bformat%5D=&filter%5Btype_mode%5D=any&filter%5Bcard_type%5D%5B10%5D=&filter%5Bpow1%5D=&filter%5Bpow2%5D=&filter%5Btuf1%5D=&filter%5Btuf2%5D=&filter%5Bconcast1%5D=&filter%5Bconcast2%5D=&filter%5Bprice_op%5D=&filter%5Bprice%5D=&filter%5Boracle_text%5D=&filter%5Bmanaprod_select%5D=any")

# wait for the page to load
wait = WebDriverWait(driver, 3)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='itemContentWrapper']")))

html = driver.page_source

soup = BeautifulSoup(html,"html.parser")


select_tag = soup.find('select', {'name': 'filter[edition]'})
options = select_tag.find_all('option')

values = [option['value'] for option in options]


df = pandas.DataFrame(values)

df.to_csv(f"sets.csv")

driver.quit()