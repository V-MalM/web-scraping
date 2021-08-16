from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Connecting to MongoDB
conn_url = "mongodb://localhost:27017"
mongo =  pymongo.MongoClient(conn_url)

# Declare the database
db = mongo.Mars_Facts

# Declare the collection
mars_data = db.mars_data


@app.route("/")
def index():
    # Fetching records. we are only creating one record and updating it with each scrape 
    # This will fetch just one record (in the form od a list) into 'results' because the collection has only one
    # Alternatively we can use find_one.
    results = mars_data.find() 

    # the results are rendered and displayed in HTML 
    return render_template("index.html", results=results)


@app.route("/scrape")
def scraper():

    # calling scrape function from scrape_mars.py 
    # It returns scraped information in the form of a dictionary into the variable 'scrape_data'
    scrape_data = scrape_mars.scrape()

    # inserting/updading mars_data collection with new scraped data
    mars_data.update_one({}, {"$set":scrape_data}, upsert=True)

    # redirecting to home page
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)