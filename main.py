from remoteok import *
from weworkremotely import *
from file import *
from flask import Flask, render_template, request


app = Flask("JobScrapper")

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    remoteok = scraping_remoteok(keyword)
    return render_template("result.html", keyword=keyword, remoteok=remoteok)

app.run("127.0.0.1")


# scraping_wwr("react")
# wwr = scraping_wwr(keyword) 

# mk_remoteok_into_csv(keyword, remoteok)