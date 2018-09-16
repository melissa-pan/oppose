####################################################################################
# Utility Functions that scrape the new article site
####################################################################################
from newspaper import Article
import score_util

####################################################################################
# news_scrape  
#   Description: 
#     opens up the url and get the contents from the site, then output keywords from 
#     the article text
#   Input:
#     url link
#     number of keywords
#   Output:
#     dictionary of keywords with scores
####################################################################################
def news_scrape(url, numKw):
    # Get web content
    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    date = article.publish_date
    text = article.text

    article.nlp()
    lib_keyword = article.keywords

    # extract search keywords from the article
    high_score_words = keywordsInDoc(text, numKw)
    keywords = get_keywords_to_crawl(title,high_score_words,lib_keyword, numKw)

    # TODO: return news info in dictionary type? which also includes publish time
    if "thestar" in url:
        return ("torontosun", keywords)
    elif "torontosun" in url:
        return ("thestar",keywords)
    else:
        raise NotImplementedError("Sorry, this news site is not currently supported yet")
