# python-webscraping
Scraping web pages using BeautifulSoup module

## Web scraping:
- It basically means extracting data from the web -- usually unstructured dada (html format) into a structured data

## Tools to use:
- `BeautifulSoup`: To parse the website's HTML and extract the data
- `python requests` : This libray will help us open the webiste's `URL`, download, and parse it to `BeautifulSoup` to extract the data

## Important Warning!:
- Always read the `Terms & Conditions` of the website. Some websites do not allow web scraping while others do

- Check the layout of the website to know what you're scraping. A change in website interface might affect your scraping

- Do not conduct aggressive scraping. This might slow down the website

## Using a User Agent:
- Since not all websites allow scraping of data using tools/programs, you can fake yoursel/program as a normal user making a request or trying to access the page. This can be done with another tool to fake yourself as someone accessing the page from chrome, safari, firefox, etc

- `pip install fake-useragent`

## Let's scrap
- We'll be scraping Jumia's page for `Names`, `Prices` and `Discounts` of smart TVs