from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape(): 
    # Setup Splinter

    # this will install the latest version each time. And will work on any sysytem.
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)  

    # this will get the exe file locally. Good for development and testing.
    # The path must be changed if it were to be executed in another system.

    # driver = r'C:\Users\vmuty\.wdm\drivers\chromedriver\win32\92.0.4515.107\chromedriver.exe'
    # browser = Browser('chrome', executable_path = driver, headless = False)
    
            
    scrape_data = {}

    # Scrape NASA Mars News
    url_redplanetscience = 'https://redplanetscience.com/'

    browser.visit(url_redplanetscience)
    time.sleep(2)    
    
    # If the website did not entirely load and failed to fetch info
    while len(browser.find_by_xpath('//div[@class="list_text"]')) == 0  :
        browser.visit(url_redplanetscience)
        #time.sleep(2) 
        browser.reload()

    html_redplanetscience = browser.html
    soup_redplanetscience = BeautifulSoup(html_redplanetscience, 'html.parser')

    results_redplanetscience = soup_redplanetscience.find('div', class_='list_text')
    news_date  = results_redplanetscience.find('div', class_='list_date').text
    news_title = results_redplanetscience.find('div', class_='content_title').text
    news_para  = results_redplanetscience.find('div', class_='article_teaser_body').text

    scrape_data["news_date"]  = news_date
    scrape_data["news_title"] = news_title
    scrape_data["news_para"]  = news_para


    # JPL Mars Space Images - Featured Image

    url_spaceimages = 'https://spaceimages-mars.com/'
    browser.visit(url_spaceimages)

    html_spaceimages = browser.html
    soup_spaceimages = BeautifulSoup(html_spaceimages, 'html.parser')
    results_spaceimages = soup_spaceimages.find('div', class_='floating_text_area')
    featured_image = results_spaceimages.find('a').text.strip().upper()

    if (featured_image != "" and featured_image == "FULL IMAGE"):
        featured_image = results_spaceimages.find('a').get('href')
    else:
        featured_image == soup_spaceimages.find('a', class_='showimg fancybox-thumbs').get('href')

    featured_image_url = url_spaceimages + featured_image
    scrape_data["featured_image_url"]  = featured_image_url


    # Mars Facts HTML Table
    
    url_galaxyfacts = 'https://galaxyfacts-mars.com'
    tables_galaxyfacts = pd.read_html(url_galaxyfacts)

    df = tables_galaxyfacts[1]
    galaxyfacts_html = df.to_html(index=False)
    galaxyfacts_html = galaxyfacts_html.replace('\n','')
    galaxyfacts_html = galaxyfacts_html.replace('class="dataframe"','class="table tablipede-str"')
    galaxyfacts_html = galaxyfacts_html.replace('<thead>    <tr style="text-align: right;">      <th>0</th>      <th>1</th>    </tr>  </thead>','')
    scrape_data["galaxyfacts_html"]  = galaxyfacts_html
    

    # Mars Hemispheres

    url_hem = 'https://marshemispheres.com/'
    browser.visit(url_hem)
    hemisphere_image_urls  = []
    url_hem_html = browser.html

    soup_url_hem_html = BeautifulSoup(url_hem_html,'html.parser')
    hem_img_divs = soup_url_hem_html.find_all('div', class_="description")
    for item in hem_img_divs:

        browser.visit(url_hem)
        
        link_text = item.find('a').text
        link_text=link_text.strip()
        
        butn = browser.find_by_text(link_text)
        butn.click()

        soup_full_res = BeautifulSoup(browser.html,'html.parser')
        full_res_div  = soup_full_res.find_all('div', class_="downloads")
        full_res_img_url = url_hem + full_res_div[0].find('a').get('href')
        
        
        url_dict = {"title":link_text, "img_url":full_res_img_url}
        hemisphere_image_urls.append(url_dict)
      
    
    scrape_data["hemisphere_image_urls"]  = hemisphere_image_urls

    browser.quit()

    return scrape_data
