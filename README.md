# Project Explanation


The entire application Urls is within the app `analystt.py`.


# Assumptions
1. Scrap data for given url `https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1`
2. Atleast for 20 pages the data need to be scraped
3. For part1 and part2 both implemented within the file,
4. Requirements like `product name`, `description`, `no of reviews`, `ratings` data are stored.


### Make a virtual enviroment
   
    Recommended python version -----> 3.9.X (The LATEST STABLE RELEASE)
    python -m venv myvenv

### Run the virtual enviroment

    myvenv\Scripts\activate.bat

### Install all dependencies

    pip install  -r requirements.txt

Run the `analystt.py` file

## Note: For scraping data from amazon found many restrictions more often the scraped data is partial and also throws the 503 status error.