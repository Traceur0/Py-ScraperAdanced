import requests
from bs4 import BeautifulSoup

# import re


def code_replacer(code):
    if code == 2:
        print("Category: Full-Stack")
    elif code == 17:
        print("Category: Front-End")
    elif code == 18:
        print("Category: Back-End")
    elif code == 4:
        print("Category: All Other Remote Jobs")
    """
        'Full-Stack': 2,
        'Front-End' : 17,
        'Back-End': 18,
        'All Other Remote Jobs': 4
        """    


def scraping_wwr(term):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        str_term = term
        print("Scraping "+str_term.upper()+f" job info in 'https://weworkremotely.com'\n")
        jobs = []
        job_code = [2, 17, 18, 4]
        for code in job_code:
            job_li = soup.select(f'#category-{code} > article > ul > li')
            try:
                job_li.pop() # for the function of the job_li list, last element is printed twice. this is resoluation
            except:
                pass
            code_replacer(code)
            for li in job_li:
                try:
                    res_company = li.select_one(f'#category-{code} > article > ul > li > a > span.company').text
                    res_title = li.select_one(f'#category-{code} > article > ul > li > a > span.title').text
                    res_jobtype = li.select(f'#category-{code} > article > ul > li > a > span.company')[1].text
                    res_location = li.select_one(f'#category-{code} > article > ul > li > a > span.region.company').text

                    # Default value
                    res_elapsed_time = ""
                    try:
                        res_elapsed_time = li.select_one(f'#category-{code} > article > ul > li > a > span.date > time').text
                    except:
                        if res_elapsed_time == None:
                            res_elapsed_time = "Recent"

                    res_link_partial = li.select(f'#category-{code} > article > ul > li > a')[0]['href']

                except:
                    try:
                        checking_err = li.select_one(f'#category-{code} > article > ul > li > a > span.title').text
                    except:
                        pass
            
                jobset = {
                    'title': res_title,
                    'company': res_company,
                    'location': res_location,
                    'jobtype': res_jobtype,
                    'elapsed_time': res_elapsed_time,
                    'apply_link': "https://weworkremotely.com" + res_link_partial
                }
                jobs.append(jobset)

            return jobs       
    else:
        print("Can't get jobs.")
