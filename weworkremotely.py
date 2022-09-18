from bs4 import BeautifulSoup
import requests
import re

'''
def link_mkr(element):
    ## applyLink는 company 스트링과 title 스트링 사이에 -(dash)를 넣고 
    ##   공백을 모두 제거 후 -로 변환, 특수문자 제거(/, (, )등 ), 알파벳 전부 소문자화 시킨 값과 같음

    de_indented = element.replace(' ', '-').replace('/', '-'). replace('.', '-') # 공백을 -로 변경
    simplified = re.sub('[^A-z0-9-]+', '', de_indented) # 특수문자 제거
    lower = simplified.lower() # 소문자화
    if "---"  in lower:
        lower = lower.replace('---', '-')
    if "--" in lower:
        lower = lower.replace('--', '-')
    return lower
'''


def scraping_wwr(term):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={term}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        str_term = term
        print("Scraping "+str_term.upper() +
              f" job info in 'https://weworkremotely.com'\n")
        jobs = []
        job_code = [2, 17, 18, 4]
        """
        'Full-Stack': 2,
        'Front-End' : 17,
        'Back-End': 18,
        'All Other Remote Jobs': 4
        """
        for code in job_code:
            job_li = soup.select(f'#category-{code} > article > ul > li')
            try:
                job_li.pop()  # for the function of the job_li list, last element is printed twice. this is resoluation
            except:
                pass
            print(code)
            for li in job_li:
                try:
                    res_company = li.select_one(
                        f'#category-{code} > article > ul > li > a > span.company').text
                    res_title = li.select_one(
                        f'#category-{code} > article > ul > li > a > span.title').text
                    res_jobtype = li.select(
                        f'#category-{code} > article > ul > li > a > span.company')[1].text
                    res_location = li.select_one(
                        f'#category-{code} > article > ul > li > a > span.region.company').text
                    res_elapsed_time = ""
                    try:
                        res_elapsed_time = li.select_one(
                            f'#category-{code} > article > ul > li > a > span.date > time').text
                    except:
                        if res_elapsed_time == None:
                            res_elapsed_time = "Recent"
                    res_link_partial = li.select(
                        f'#category-{code} > article > ul > li > a')[0]['href']
                except:
                    try:
                        checking_err = li.select_one(
                            f'#category-{code} > article > ul > li > a > span.title').text
                    except:
                        pass
                # company_trimmed = link_mkr(res_company)
                # title_trimmed = link_mkr(res_title)
                # apply_link = company_trimmed + "-" + title_trimmed
                # print(apply_link)

                jobset = {
                    'title': res_title,
                    'company': res_company,
                    'location': res_location,
                    'jobtype': res_jobtype,
                    'elapsed_time': res_elapsed_time,
                    'apply_link': "https://weworkremotely.com" + res_link_partial
                }
                print(jobset)
                # jobs.append(jobset)

    else:
        print("Can't get jobs.")
