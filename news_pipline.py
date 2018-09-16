####################################################################################
# Main Function to run backend script after user init the plugin
####################################################################################
from news_scraper import news_scrape
from find_related import find_related_articles

def news_pipline(url):
    """
    Description:
       Ingest a list of news article with opposing views from the newssite that sit
       at the different side of the political scale. 
    """
    num_keyword = 3
    (news,keyword) = news_scrape(url, num_keyword)
    find_related_articles(news, keyword)

if __name__ == "__main__":
    news_pipline("https://www.thestar.com/")