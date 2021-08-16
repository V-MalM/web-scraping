# Web Scraping Project - Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the process.

## Step 1 - Scraping

Completed scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and built code to complete all scraping and analysis tasks. The following outlines what data was scraped.

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collected the latest News Title and Paragraph Text. Stored the text to variables. Also scraped the date of the article.

<details>
<summary><strong>Click to see an example!</strong></summary>

```python

# Example:
news_date = "August 16, 2021"
news_title = "Two Rovers to Roll on Mars Again: Curiosity and Mars 2020"
news_p = "They look like twins. But under the hood, the rover currently exploring the Red Planet and the one launching there this summer have distinct science tools and roles to play."

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
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'

```

### Mars Facts

* Visited the Mars Facts webpage [here](https://galaxyfacts-mars.com) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

* Saved the HTML string to a variable 'galaxyfacts_html'.

<details>
<summary><strong>Click to see an example!</strong></summary>

```python

# Example:
galaxyfacts_html = "<table border="1" class="table tablipede-str">
        <tbody>
            <tr>
                <td>Equatorial Diameter:</td>
                <td>6,792 km</td>
            </tr>
            <tr>
                <td>Polar Diameter:</td>
                <td>6,752 km</td>
            </tr>
            <tr>
                <td>Mass:</td>
                <td>6.39 × 10^23 kg (0.11 Earths)</td>
            </tr>
            <tr>
                <td>Moons:</td>
                <td>2 ( Phobos &amp; Deimos )</td>
            </tr>
            <tr>
                <td>Orbit Distance:</td>
                <td>227,943,824 km (1.38 AU)</td>
            </tr>
            <tr>
                <td>Orbit Period:</td>
                <td>687 days (1.9 years)</td>
            </tr>
            <tr>
                <td>Surface Temperature:</td>
                <td>-87 to -5 °C</td>
            </tr>
            <tr>
                <td>First Record:</td>
                <td>2nd millennium BC</td>
            </tr>
            <tr>
                <td>Recorded By:</td>
                <td>Egyptian astronomers</td>
            </tr>
        </tbody>
    </table>"

```
</details>
<br />
### Mars Hemispheres

* Visited the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* Wrote a loop to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


<details>
<summary><strong>Click to see an example!</strong></summary>

```python

# Example:
hemisphere_image_urls = [{'title': 'Cerberus Hemisphere Enhanced',
  'img_url': 'https://marshemispheres.com/images/full.jpg'},
 {'title': 'Schiaparelli Hemisphere Enhanced',
  'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'},
 {'title': 'Syrtis Major Hemisphere Enhanced',
  'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'},
 {'title': 'Valles Marineris Hemisphere Enhanced',
  'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'}]

```
</details>
<br />

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