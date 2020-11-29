from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

#flask connection to Mondo_DB
app.config["mongodb_url"] = "mongodb://localhost:27017/mars_app"
app = Flask(__name__)

# route ti index.html
@app.route("/")
def home():
    mars_data = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict = mars_dict)
app.route("/scrape")
def scrape():















#end instance of Flask
if __name__ == "__main__":
    app.run(debug=True)
