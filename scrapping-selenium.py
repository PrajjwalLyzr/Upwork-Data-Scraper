import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

page_no = 7 # just change the number after every run

url = f"""https://www.upwork.com/nx/search/jobs/?page={page_no}&per_page=50&q=%28ChatGP,%20OR%20Langchain,%20OR%20Crewai,%20OR%20Claude,%20OR%20Llamaindex,%20OR%20Autogen,%20OR%20Cohere%29&sort=recency"""
val = url
wait = WebDriverWait(driver, 20)
driver.get(val)


def scraper():
    job_titles = []
    job_description = []
    job_links = []

    titles = driver.find_elements(by=By.XPATH, value="""  //*[@class="air3-line-clamp is-clamped"]/h2 """)
    descriptions = driver.find_elements(by=By.XPATH, value= """ //*[@class="air3-line-clamp is-clamped"]/p """)
    links = driver.find_elements(by=By.XPATH, value=""" //*[@class="air3-line-clamp is-clamped"]/h2/a """)
    
   

    for i in range(len(titles)):
        job_titles.append(titles[i].text)
        job_description.append(descriptions[i].text)
        job_links.append(links[i].get_attribute('href'))
        

    
    return job_titles, job_description, job_links



def csv_maker(titles, description, links, filename):
    data_items = {
        'Titles':titles,
        'Job Description':description,
        'Links':links
    }

    df = pd.DataFrame(data_items)
    df.to_csv(f"{filename}_jobs.csv", index=False)




job_titles, job_descriptions, job_links = scraper()
csv_maker(titles=job_titles, description=job_descriptions, links=job_links, filename=f'UpWorkData{page_no}')
