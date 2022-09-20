from ast import keyword
from re import search
from remoteok import *
from weworkremotely import *
from file import *
from flask import Flask, render_template


code = 200

app = Flask("JobScrapper")

@app.route("/")
def main():
    return render_template("home.html", search=keyword)

@app.route("/search")
def search():
    return

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