from bs4 import BeautifulSoup as BS
import requests


def scraping_remoteok(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BS(request.text, "html.parser")
        print("Scraping "+term.upper()+f" job info in '{url}'\n")
        jobs = []
        ad = soup.select_one('tr.sw-insert.ad.advertisement.sponsored')
        job_table = soup.select('tr.job') # array, resultType
        job_table.insert(0, ad)
        for item in job_table:
            title = item.select_one(
                'tr > td.company.position.company_and_position > a > h2').text.strip('\n')
                # jobsboard > tbody > tr.sw-insert.ad.advertisement.sponsored > td.company.position.company_and_position > a:nth-child(3) > h3
            company = item.select_one(
                'tr > td.company.position.company_and_position > a > h3').text.strip('\n ')

            try:
                verified = item.select_one(
                    'tr > td.company.position.company_and_position > span.verified.tooltip').text
            except:
                verified = ""

            # Default value # 
            location = []
            salary = ""
            jobtype = ""
            tag = []
            for idx in range(4):
                try:
                    loc = item.select(
                        'tr > td.company.position.company_and_position > div.location')[idx].text
                    if "💰" in loc:
                        salary = loc
                    elif "⏰" in loc:
                        jobtype = loc
                    else:
                        location.append(loc)
                except:
                    break

            for idx in range(0, 3):
                try:
                    tag_list = item.select(f'tr > td.tags > a > div > h3')[
                        idx].text.strip('\n')
                    tag.append(tag_list)
                except:
                    pass

            try:
                elapsed_time = item.select_one(
                'tr > td.time > time').text.strip('\n')
            except:
                elapsed_time = "Unknown"

            try:
                closed = item.select_one(
                    'tr > td.company.position.company_and_position > span.closed').text.upper()
            except:
                closed = ""

            try:
                apply_id = item.select_one('tr > td.source > a')['href']
                link = f"https://remoteok.com{apply_id}"
            except:
                link = "Recruitment closed"

            jobset = {
                'title': title,
                'company': company,
                'location': location,
                'jobtype': jobtype,
                'elapsed_time': elapsed_time,
                'apply_link': link,
                'salary': salary,
                'tag': tag,
                'verified': verified,
                'closed': closed
            }
            jobs.append(jobset)

        return jobs
    else:
        print("Can't get jobs.")
