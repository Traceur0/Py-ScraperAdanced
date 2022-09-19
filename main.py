from remoteok import *
from weworkremotely import *


# scraping_remoteok("rust")
# scraping_wwr("react")

def transmitter():
    return input("type what you search for: ")


keyword = transmitter()

remoteok = scraping_remoteok(keyword)
# wwr = scraping_wwr(keyword)

jobset_remoteok = {
                'title': res_title.string,
                'company': res_company.string,
                'location': res_location.string,
                'jobtype': res_jobtype.string,
                'elapsed_time': res_elapsed_time.string,
                'apply_link': link,
                'salary': res_salary,
                'tag': res_tag,
                'verified': res_verified,
                'closed': res_closed
            }
jobset_wwr = {
                    'title': res_title,
                    'company': res_company,
                    'location': res_location,
                    'jobtype': res_jobtype,
                    'elapsed_time': res_elapsed_time,
                    'apply_link': "https://weworkremotely.com" + res_link_partial
                }

# Making file for RemoteOk.com
file = open(f"{keyword}.csv", "w", encoding = "utf-8")
file.write("title, company, location, jobtype, elapsed_time, apply_link, salary, tag, verified, closed")

for unit in remoteok:
    file.write(f"""{jobset_remoteok['title']}, 
                {jobset_remoteok['company']}, 
                {jobset_remoteok['location']}, 
                {jobset_remoteok['jobtype']}, 
                {jobset_remoteok['elapsed_time']},
                {jobset_remoteok['apply_link']},
                {jobset_remoteok['salary']},
                {jobset_remoteok['tag']},
                {jobset_remoteok['verified']},
                {jobset_remoteok['closed']}\n
                """)
    file.close()

# Making file for WeWorkRemotely.com
file = open()