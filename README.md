# Python Web Script for crawling NSL lighting website for product data
I used scripts like these all the time to parse vendor data from ecommerce websites. This script parses a site and outputs a nicely formatted csv to upload to our shopping platform.

# Python and scrapy offer a powerful way to retreive data online. 

# Getting Started

First you will want to install scrapy. If you are on windows the easiest way is to install Anaconda and then follow the scrappy command line instructions to install and setup a new project. 
https://docs.anaconda.com/anaconda/install/windows/

This can be done witht he following commands when Anaconda is installed
```
conda install -c conda-forge scrapy
```

Once you setup the project you can simple add the product_data.py file to your spiders folder

Open the terminal from Anaconda and cd into your project directory. The spiders directory should be one level down.

Below command will crawl the pages in the start_urls and display the results
```
scrapy crawl products   
```

Below command will output the data to a csv product_file.csv in your project folder
```
scrapy crawl products -o product_file.csv -t csv
```
And now we have a nice spreadsheet of images, files and descriptions to update our online catalog with when the vendor is no help!

A sample csv of the results from all products on their website is located in the nsl project folder for reference. 

need help trying to scrape data for your online store? Scripts like these can help, and feel free to ask me if you need additional help!
