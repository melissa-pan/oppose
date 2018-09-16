####################################################################################
# Main Function to run backend script after user init the plugin
####################################################################################
import news_scrape from news_scraper

def news_pipline(url):
    num_keyword = 3
    news_scrape(url, num_keyword)
    # sebasian's function
    # get opposing ling
    # ....