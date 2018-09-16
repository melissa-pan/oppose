import urllib.request

from bs4 import BeautifulSoup


def _get_search_html(domain_name, keywords, keyword_separator):
    """
    _get_search_html searches the domain_name database for somewhat relevant articles

    :param domain_name: a str that designates a news outlet query url
    :param keywords: a list of keywords to insert int the query
    :param keyword_separator: a string that separates the keywords in the query
    :return: a BeautifulSoup parse of the search results page
    """
    url = domain_name
    keywords = " ".join(keywords).replace(" ", keyword_separator)
    url += keywords
    return BeautifulSoup(urllib.request.urlopen(url), 'html.parser')


def get_article_urls(keywords, site):
    article_urls = {}

    if site == "toronto star":
        first_html_child = 0
        soup = _get_search_html("https://www.thestar.com/search.html?q=", keywords, "%20")

        # extract stories to crawl
        for article in soup.find_all("div", {"class": "story__body"}):
            article_urls["https://www.thestar.com" + article
                .contents[first_html_child].contents[first_html_child]
                .contents[first_html_child].get('href')] = 0

    elif site == "toronto sun":
        soup = _get_search_html("https://torontosun.com/?s=", keywords, "+")

        # extract stories to crawl
        for article in soup.find_all('article'):
            article_urls[article.contents[1].contents[1].get('href')] = 0

    else:
        print("error: this website is not supported")
        exit(1)

    return article_urls


def find_related_articles(keywords, site):
    article_urls = get_article_urls(keywords, site)
    print (article_urls)


if __name__== '__main__':
    find_related_articles(["climate", "change"], "toronto star")