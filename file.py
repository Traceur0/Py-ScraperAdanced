from time import time, localtime, strftime



init = strftime('%y%m%d%H%M', localtime(time()))

def mk_remoteok_into_csv(keyword, remoteok):
    # Making file for RemoteOk.com
    file = open(f"remoteok_{keyword}_{init}.csv", "wt", encoding="utf-8-sig")
    file.write("title,company,location,jobtype,elapsed_time,apply_linksalary,tag,verified,closed\n")

    for jobset in remoteok:
        file.write(f"{jobset['title']}, {jobset['company']}, {jobset['location']}, {jobset['jobtype']}, {jobset['elapsed_time']},{jobset['apply_link']},{jobset['salary']},{jobset['tag']},{jobset['verified']},{jobset['closed']}\n ")
    file.close()


def mk_wwr_into_csv(keyword, wwr):
    # Making file for WeWorkRemotely.com
    file = open(f"weworkremotely_{keyword}_{init}.csv", "wt", encoding = "utf-8-sig")
    file.write("title, company, location, jobtype, elapsed_time, apply_link\n")

    for jobset in wwr:
        file.write(f"{jobset['title']},{jobset['company']},{jobset['location']},{jobset['jobtype']},{jobset['elapsed_time']},{jobset['apply_link']}\n")
    file.close()