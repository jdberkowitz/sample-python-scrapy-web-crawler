import scrapy

class QuotesSpider(scrapy.Spider):
    # We name our spider with the name variable, this is what we reference on the cmd line to run our crawl
    name = "products"
    # Here we can add a list of URLs to crawl. 
    # I chose to do them manually becuase i wanted to see each page and there isn't to many on this website.
    # This script was written on Jan 3 2019 so if reading this in the future 
    #
    # (or even spookier ... in the past) then you may want to reference the wayback machine archive to see the page markup correctly
    start_urls = [
        '../product-41.html', # Pages contained in the root of the project are from https://www.nslusa.com/products/41/
        '../product-43.html', # Replcae these with relative links to the files or use the live url of your target
    ]
    
    # Our parse function will crawl the pages of the start_urls and return a response that is handled in the body of the function
    def parse(self, response):        
            for product in response.css('div.content-body'):  
                ##Setup the base url for the image and file paths
                base_url = "https://www.nslusa.com"             
                ##Grab a list of the image urls 
                images_list = product.css('.h-100::attr(href)').extract()
                ##Grab a list of the pdf and eps files
                pdf_link_list = product.css('.btn-sm::attr(href)').extract()
                ##Create a dictionary of the the images using a base string and the index for the key
                imageDict = {
                    ##Here we are simply converting the index i to a string so we can concatenate it into a column header
                    ##We also strip the hash off the url and concatenate the base url to get fully qualified domain name (FQDN)
                    ##We use enumerate to create the index of the list in the for in loop
                   'additional_image_url_' + str(i): base_url + key.strip('#') for i, key in enumerate(images_list)
                }
                    ##We do the same thing as above for the spec files. 
                    ##TO-DO! Sperate the files by file type into seperate columns
                pdfLinkDict = {
                    'spec_or_ies_file_url_' + str(i): base_url + key for i, key in enumerate(pdf_link_list)
                }
                ##Now we create our main product dictionary by taking elements within the main body
                productsDict = {
                    ##Using the css selector we can grab the text 
                    'name': product.css('h5::text').extract_first(),
                    ##We can get pretty granular with our selectors. Checkout SelectorGadget extentsion for chrome to quickly identify css selectors
                    'description': product.css('p:nth-child(1)').extract_first(),
                    ##This is our main product picture and we create a FQDN
                    'main_image_url': base_url + product.css('.flex-md-nowrap .mx-auto img::attr(src)').extract_first(),
                    ##Here we are just putting our image list into a column just for reference
                    'additional_images_list': images_list,
                    ##Same with the remaining file types
                    'all_pdf_ies_links_list': pdf_link_list,
                    ##I wanted the HTML of the description and the appilcation so i can reuse it on my project but you may just want text so modify by using the psuedo element
                    'applications_html': product.css('#product-applications').extract_first(),
                    ##For the brochure link we follow the same as the main image
                    'product_brochure_pdf_url': base_url + product.css('.mt-md-0 a::attr(href)').extract_first()
                }
                ##Finally we use update to add the image and file columns with the FQDN's back to the product dictionary 
                productsDict.update(pdfLinkDict)
                productsDict.update(imageDict)
                ##Yield completes our generator and returns the output with nice column names and FQDNs to use
            yield productsDict

