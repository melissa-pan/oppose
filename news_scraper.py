from newspaper import Article
import score_util

####################################################################################
# news_scrape  
#   Description: 
#     opens up the url and get the contents from the site, then output keywords from 
#     the article text
#   Input:
#     url link
#   Output:
#     dictionary of keywords with scores
####################################################################################
def news_scrape(url):
    # Get web content
    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    date = article.publish_date
    text = article.text

    # extract search keywords from the article 
    high_score_words = keywordsInDoc(text, 5)
    keywords = get_keywords_to_crawl(title,high_score_words)

    if "thestar" in url:
        return ("torontosun", keywords)
    else "torontosun" in url:
        return ("thestar",keywords)
    else:
        raise NotImplementedError("Sorry, this news site is not currently supported yet")
