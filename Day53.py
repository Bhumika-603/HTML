from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements] 
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)
print("\n")

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements] 
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)
print("\n")

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)
print("\n")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScz86Mu61819VhIuYy9Sxlds0iwThpDoggxv63iyFe07Mc5kQ/viewform")
    time.sleep(2)

    address = driver.find_element(by=By.XPATH, 
                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, 
                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    submit_button = driver.find_element(by=By.XPATH, 
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()

# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import requests
# import time

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

# url = "https://appbrewery.github.io/Zillow-Clone/"
# response = requests.get(url=url, headers=header)

# data = response.text
# soup = BeautifulSoup(data, "html.parser")

# # Extracting data
# all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
# all_links = [link["href"] for link in all_link_elements]

# all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
# all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

# all_price_elements = soup.select(".PropertyCardWrapper span")
# all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements]

# # Setting up Selenium WebDriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# form_url = "https://docs.google.com/forms/d/e/1FAIpQLScz86Mu61819VhIuYy9Sxlds0iwThpDoggxv63iyFe07Mc5kQ/viewform"

# # Filling the form
# for n in range(len(all_links)):
#     driver.get(form_url)

#     try:
#         # Wait for fields to load
#         address = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, 
#                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
#         )
#         price = driver.find_element(By.XPATH, 
#                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#         link = driver.find_element(By.XPATH, 
#                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
#         submit_button = driver.find_element(By.XPATH, 
#                 '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

#         # Fill form
#         address.send_keys(all_addresses[n])
#         price.send_keys(all_prices[n])
#         link.send_keys(all_links[n])
#         submit_button.click()

#         print(f"Submitted entry {n+1}/{len(all_links)} successfully.")
#         time.sleep(2)  # Small delay between submissions

#     except Exception as e:
#         print(f"Error occurred for entry {n+1}: {e}")

# # Close browser after all submissions
# driver.quit()
