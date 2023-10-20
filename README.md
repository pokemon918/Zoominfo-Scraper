# Zoominfo-Scrapping
Simple scraper for collecting data about the companies specified in the `input.csv` file from
the https://www.zoominfo.com/ website. 

## About
The scraper collects the following data about companies:

* Headquarters
* Phone
* Revenue
* Number of employees
* Website

As a result, it generates a separate CSV file for every company from the input list. These files are 
located in the `output` folder. Each filename is created using the name of the company - {company_name}.csv.
For example - Amazon.csv, Google.csv, etc.

## Technologies
* Scrapy 2.3.0
* scrapy-rotating-proxies 0.6.2
* rotating-free-proxies 0.1.2

## How to install and run
1. Clone the repo: `git clone https://github.com/dfesenko/zoominfo_scraper.git`. 
Go inside the `zoominfo_scraper` folder: `cd zoominfo_scraper`.
2. Create a virtual environment: `python -m venv venv`.
3. Activate virtual environment: `source venv/bin/activate`.
4. Install dependencies into the virtual environment: 
`pip install -r requirements.txt`.
5. Change directory: `cd zoominfo`.
6. Create or change the `input.csv` file. Place there the names of the companies you want 
to parse.
7. Issue the following command: `scrapy crawl zoominfo`.
8. Now the script should be started. The `output` directory should 
appear in the directory. The script populates it with files (one csv file per company). 
9. If you want to change some scrapper parameters you can explore the 
`/zoominfo/zoominfo/settings.py` file. 

## Notes about proxies
The scraper uses `scrapy-rotating-proxies` and `rotating-free-proxies` packages to get the list of 
available free proxies and rotate them automatically. You can turn off this feature by commenting out 
the `DOWNLOADER_MIDDLEWARES` variable in the `settings.py` file. Also, during the work, these libraries 
create the `proxies.txt` file in the root of the project. There are a list of free proxies stored.
