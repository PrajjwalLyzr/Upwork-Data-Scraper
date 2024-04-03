import pandas as pd
import os
import time
from dotenv import load_dotenv; load_dotenv()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

# Open Chrome in incognito mode
chrome_options.add_argument("--incognito")

# chrome_options.add_argument("--headless")  # Enable headless mode

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

Id = os.getenv('ID')
Password = os.getenv('PASSWORD')

BASE_URL = "https://www.upwork.com/ab/account-security/login"

driver.get(BASE_URL)

wait = WebDriverWait(driver, 10)


# username_field = driver.find_element(by=By.XPATH, value=""" //*[@id="login_username"] """)
username_field = wait.until(EC.visibility_of_element_located((By.XPATH, """ //*[@id="login_username"] """)))
username_field.send_keys(Id)

time.sleep(3)

# continue_button = driver.find_element(by=By.XPATH, value=""" //*[@id="login_password_continue"] """)
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, """ //*[@id="login_password_continue"] """)))
continue_button.click()

time.sleep(3)

password_filed = wait.until(EC.visibility_of_element_located((By.XPATH, """ //*[@id="login_password"] """)))
checkbox = wait.until(EC.element_located_to_be_selected((By.XPATH, """//*[@id="login"]/div/div/div[1]/div[5]/div/div[1]/div/label/span""")))
if not checkbox.is_selected():
    checkbox.click()

time.sleep(3)


new_page_url = driver.current_url

# Print the URL of the page after login
print("URL after login:", new_page_url)


# password_field = driver.find_element(by=By.ID, value="login_password")
# checkbox = driver.find_element(by=By.XPATH, value="""//*[@id="login"]/div/div/div[1]/div[5]/div/div[1]/div/label/span""")
# if not checkbox.is_selected():
#     checkbox.click()

# password_field.send_keys(Password)
# login_button = driver.find_element(By.XPATH, value=""" //*[@id="login_control_continue"] """)



# Click the submit button
# login_button.click()



# page_no = 1 # just change the number after every run

# url = f"""https://www.upwork.com/nx/search/jobs/?page={page_no}&per_page=50&q=%28ChatGP,%20OR%20Langchain,%20OR%20Crewai,%20OR%20Claude,%20OR%20Llamaindex,%20OR%20Autogen,%20OR%20Cohere%29&sort=recency"""
# val = url
# wait = WebDriverWait(driver, 20)
# driver.get(val)


# def scraper():
#     job_titles = []
#     job_description = []
#     job_links = []

#     titles = driver.find_elements(by=By.XPATH, value="""  //*[@class="air3-line-clamp is-clamped"]/h2 """)
#     descriptions = driver.find_elements(by=By.XPATH, value= """ //*[@class="air3-line-clamp is-clamped"]/p """)
#     links = driver.find_elements(by=By.XPATH, value=""" //*[@class="air3-line-clamp is-clamped"]/h2/a """)
    
   

#     for i in range(len(titles)):
#         job_titles.append(titles[i].text)
#         job_description.append(descriptions[i].text)
#         job_links.append(links[i].get_attribute('href'))
        

    
#     return job_titles, job_description, job_links



# def csv_maker(titles, description, links, filename):
#     data_items = {
#         'Titles':titles,
#         'Job Description':description,
#         'Links':links
#     }

#     df = pd.DataFrame(data_items)
#     df.to_csv(f"data/{filename}_jobs.csv", index=False)




# job_titles, job_descriptions, job_links = scraper()
# csv_maker(titles=job_titles, description=job_descriptions, links=job_links, filename=f'UpWorkData{page_no}')
