from bs4 import BeautifulSoup as BS
import requests


def scraping_remoteok(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BS(request.text, "html.parser")
        print("Scraping "+term.upper()+f" job info in '{url}'\n")
        jobs = []
        tbody = soup.select('tr.job')
        for item in tbody:
            res_company = item.select_one(
                'tr > td.company.position.company_and_position > span.companyLink > h3').text.strip('\n ')
            res_title = item.select_one(
                'tr > td.company.position.company_and_position > a > h2').text.strip('\n')
            try:
                res_verified = item.select_one(
                    'tr > td.company.position.company_and_position > span.verified.tooltip').text
            except:
                res_verified = ""
            res_location = []  # DEFAULT
            res_salary = ""  # DEFAULT
            res_rule = ""  # DEFAULT
        for idx in range(4):
            try:
                loc = item.select(
                    'tr > td.company.position.company_and_position > div.location')[idx].text
                if "💰" in loc:
                    res_salary = loc
                elif "⏰" in loc:
                    res_jobtype = loc
                else:
                    res_location.append(loc)
            except:
                break
            res_tag = []
        for idx in range(0, 3):
            try:
                res_tag_child = item.select(f'tr > td.tags > a > div > h3')[
                    idx].text.strip('\n ')
                res_tag.append(res_tag_child)
            except:
                pass
            res_elapsed_time = item.select_one(
                'tr > td.time > time').text.strip('\n ')
            try:
                res_closed = item.select_one(
                    'tr > td.company.position.company_and_position > span.closed').text
            except:
                res_closed = ""
        try:
            apply_id = item.select_one('tr > td.source > a')['href']
            link = f"https://remoteok.com{apply_id}"
        except:
            link = "Recruitment closed"
        jobset = {
            'title': res_title,
            'company': res_company,
            'location': res_location,
            'jobtype': res_jobtype,
            'elapsed_time': res_elapsed_time,
            'apply_link': link,
            'salary': res_salary,
            'tag': res_tag,
            'verified': res_verified,
            'closed': res_closed
        }
        print(jobset)
        print("\n")
        print("End Of Line\n\n\n")
        # jobs.append(jobset)
    else:
        print("Can't get jobs.")
