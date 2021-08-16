# Web Scraping Project - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the process.

## Step 1 - Scraping

Completed scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, MongoDB.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and built code to complete all scraping and analysis tasks. The following outlines what data was scraped.

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Stored the text to variables. Also scraped the date of the article which is ofcourse, the current date.


<details>
<summary><strong>Click to see code!</strong></summary>

```python

# Example:
news_date = "08/16/2021"
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."


```
</details>

<br />


### JPL Mars Space Images - Featured Image

* Visited url for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Searched for full size `.jpg` image.

* Saved the url string for this image.

```python
# Example:
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
```

### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

* Saved the HTML string to a variable 'galaxyfacts_html'.

### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* Wrote a loop to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting  Jupyter notebook into a Python script called `scrape_mars.py`. Created a function called `scrape` that will execute all scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, createed a route called `/scrape` that will import `scrape_mars.py` script and call  `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

* Used bootstarp for HTML template and css for styling the template.

![final_app_part1.png](Images/final_app.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.