from unittest import skip
import requests 
from bs4 import BeautifulSoup

URL = "https://www.indeed.co.uk/jobs?q=software+developer&l=Hatfield"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser') 
results = soup.find(id='mosaic-provider-jobcards')
#print(results.prettify())
job_elems = results.find_all('div', class_='job_seen_beacon') 

for job_elem in job_elems: 
    title_elem = job_elem.find('h2', class_="jobTitle")
    print(title_elem.text.strip(), end="\n"*2)

    company_elem = job_elem.find('span', class_="companyName")
    print(company_elem.text.strip(), end="\n"*2)

    location_elem = job_elem.find('div', class_="companyLocation")
    print(location_elem.text.strip(), end="\n"*2)
    
    if job_elem.find('span', class_="ratingNumber") == None:
        rating_elem = "No rating provided withi this job listing"
    else: 
        rating_elem = job_elem.find('span', class_="ratingNumber")
        print(rating_elem.text.strip(), end="\n"*2)
    
    if job_elem.find('div', class_="salary-snippet") == None: 
        salary_elem = "No salary provided for this job listing"
    else:
        salary_elem = job_elem.find('div', class_="salary-snippet")
        print(salary_elem.text.strip(), end="\n"*2)
    
    jobDesc_elem = job_elem.find('div', class_="job-snippet")
    print(jobDesc_elem.text.strip(), end="\n"*2)

    #print("Apply at", links[count], end="\n"*2)


    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------", end="\n"*2)
    
    
    
    
    
    