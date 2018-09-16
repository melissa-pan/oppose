####################################################################################
# Main Function to run backend script after user init the plugin
####################################################################################
from news_scraper import news_scrape
from find_related import find_related_articles

def news_pipline(url):
    num_keyword = 3
    data = news_scrape(url, num_keyword)
    find_related_articles(data[1], data[0])

if __name__ == "__main__":
    news_pipline("thestar")