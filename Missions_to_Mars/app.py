from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

conn_url = "mongodb://localhost:27017"
mongo =  pymongo.MongoClient(conn_url)

# Declare the database
db = mongo.mars_data

# Declare the collection
mars_data = db.mars_data


@app.route("/")
def index():
    # Fetching records. we are only creating one record and updating it with each scrape 
    # so this will fetch just one record in to the results list. Alternatively we can use find_one
    results = mars_data.find() 
    
    return render_template("index.html", results=results)


@app.route("/scrape")
def scraper():

    scrape_data = scrape_mars.scrape()
    mars_data.update_one({}, {"$set":scrape_data}, upsert=True)
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)