def mk_remoteok_into_csv(keyword, remoteok):
    # Making file for RemoteOk.com
    file = open(f"{keyword}.csv", "w", encoding = "utf-8")
    file.write("title, company, location, jobtype, elapsed_time, apply_link, salary, tag, verified, closed")

    for jobset in remoteok:
        file.write(f"""{jobset['title']}, 
                    {jobset['company']}, 
                    {jobset['location']}, 
                    {jobset['jobtype']}, 
                    {jobset['elapsed_time']},
                    {jobset['apply_link']},
                    {jobset['salary']},
                    {jobset['tag']},
                    {jobset['verified']},
                    {jobset['closed']}\n 
                    """)
        file.close()


def mk_wwr_into_csv(keyword, wwr):
    # Making file for WeWorkRemotely.com
    file = open(f"{keyword}.csv", "w", encoding = "utf-8")
    file.write("title, company, location, jobtype, elapsed_time, apply_link\n")

    for jobset in wwr:
        file.write(f"""{jobset['title']},
                    {jobset['company']},
                    {jobset['location']},
                    {jobset['jobtype']},
                    {jobset['elapsed_time']},
                    {jobset['apply_link']}\n
                    """)
        file.close()