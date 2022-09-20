from remoteok import *
from weworkremotely import *
from file import *
from flask import Flask


app = Flask("JobScrapper")

@app.route("/")
def main():
    return 'MAIN'

@app.route("/test")
def test():
    return 'TEST PAGE'

app.run("127.0.0.1")



# scraping_remoteok("rust")
# scraping_wwr("react")
'''
def transmitter():
    return input("type what you search for: ")
keyword = transmitter()

remoteok = scraping_remoteok(keyword)
mk_remoteok_into_csv(keyword, remoteok)
'''
# wwr = scraping_wwr(keyword)