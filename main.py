from remoteok import *
from weworkremotely import *
from file import *
from flask import Flask, render_template, request, redirect, send_file


app = Flask("JobScrapper")

database = {}

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in database:
        remoteok = database[keyword]
    else:
        remoteok = scraping_remoteok(keyword)
        database[keyword] = remoteok
    return render_template("result.html", keyword=keyword, remoteok=remoteok)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in database:
        return redirect(f"/search?keyword={keyword}")
    mk_remoteok_into_csv(keyword, database[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1")


# scraping_wwr("react")
# wwr = scraping_wwr(keyword) 

# mk_remoteok_into_csv(keyword, remoteok)