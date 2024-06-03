from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = r'C:/Users/g6-te/Downloads/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)
# Open the webpage
website = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
driver.get(website)

# Add a delay to allow the page to load
time.sleep(5)  # Wait for 5 seconds

# Find all match rows
matches = driver.find_elements(By.CSS_SELECTOR, ".product-wrapper.card-body")

rate = []
product_name = []

for match in matches:
    #print(match.text)
    #print(match.find_elements(By.XPATH, "./ div[@ class ='caption'] / h4[1]").text)
    #product_name.append(match.find_elements(By.XPATH, "./ div[@ class ='caption'] / h4[2]"))
    caption_elements = match.find_elements(By.XPATH, "./div[@class='caption']/h4")
    if caption_elements:
        print(caption_elements[0].text)
        a_element = caption_elements[1].find_element(By.TAG_NAME, "a")
        title = a_element.get_attribute("title")
        print(title)
        rate.append(caption_elements[0].text)
        product_name.append(title)
    else:
        print("No caption elements found")

# Create a DataFrame from the extracted data
df = pd.DataFrame({'ProductName': product_name,'Rate': rate})

df['Product_List'] = df['ProductName'] + " - " + df['Rate']

df = df[['Product_List']]
# Save the DataFrame to a CSV file
df.to_csv('computer.txt')

print(df)
