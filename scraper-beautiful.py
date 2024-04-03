from bs4 import BeautifulSoup
from html_content import html_content
import pandas as pd

def scraper():
    job_title = []
    job_links = []
    soup = BeautifulSoup(html_content, "html.parser")

    titles = soup.find_all('h2', {'class':"h5 mb-0 mr-2 job-tile-title"})
    for title in titles:
        job_title.append(title.text)
        links = title.find('a')
        links = 'https://www.upwork.com' + str(links['href'])
        job_links.append(links)

    return job_title, job_links


def csv_maker(titles, links, filename):
    data_items = {
        'Titles':titles,
        'Links':links
    }

    df = pd.DataFrame(data_items)
    df.to_csv(f"data/{filename}_jobs.csv", index=False)

if __name__ == "__main__":
    count = 3
    titles, links = scraper()
    csv_maker(titles=titles, links=links, filename=f'UpWorkJobData{count}')