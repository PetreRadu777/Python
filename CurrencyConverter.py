from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import requests

driver = webdriver.Chrome()
driver.get("https://freecurrencyapi.com/")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[1]/div/div[3]/a[1]").click()
driver.find_element(By.ID, "email").send_keys("Petre.radu94@gmail.com")
driver.find_element(By.ID, "password").send_keys("Petreradu94")
driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[4]/button/span').click()

# Click the button to copy the API key to the clipboard
copy_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/div[2]/div[1]/div/div/div/div/div[2]/button')
copy_button.click()

# Retrieve the API key from the clipboard
API_KEY = pyperclip.paste()

# Retrieve and print the BASE URL
base_url_element = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/main/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/span[2]/div/div/button')
base_url_element.click()
BASE_URL = pyperclip.paste()

NEW_BASE_URL= BASE_URL.split('=')[0] + '=' + API_KEY

print("BASE URL:", NEW_BASE_URL)
print("API Key:", API_KEY)

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{NEW_BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        # print(data)
        return data["data"]
    except Exception as e:
        print("Invalid data")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break
    data = convert_currency(base)
    if not data:
        continue
    del data[base]
    # print(data)
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

input("Press Enter to close the browser...")
