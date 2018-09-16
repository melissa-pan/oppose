import urllib.request
import datetime
from time import sleep

from bs4 import BeautifulSoup

def _relevent_date_star(article_info, article_date):
    seconds_per_3_weeks = datetime.timedelta(seconds=604800)
    url = article_info["url"]

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    alt_article_date = soup.find_all("meta", {"name": "parsely-pub-date"})[0]['content']
    alt_article_date = datetime.datetime.strptime( alt_article_date, "%Y-%m-%dT%H:%M:%S.%fZ" )
    if (article_date - alt_article_date) >= seconds_per_3_weeks:
        return True #TODO: fix dattime
    return True

def _relevent_date_sun(article_info, article_date):
    seconds_per_3_weeks = datetime.timedelta(seconds=604800)
    url = article_info["url"]

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    alt_article_date = soup.find_all("time", {"class": "updated"})[0]['datetime'][0:-6]

    alt_article_date = datetime.datetime.strptime( alt_article_date, "%Y-%m-%dT%H:%M:%S" )
    if (article_date - alt_article_date) >= seconds_per_3_weeks:
        return True #TODO: fix dattime
    return True



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
    print(url)
    return BeautifulSoup(urllib.request.urlopen(url), 'html.parser')


def find_related_articles(data, keywords):
    article_data = []
    site = data['domain']
    date = data['date']
    if site == "thestar":
        first_html_child = 0
        soup = _get_search_html("https://www.thestar.com/search.html?sortby=relevance&sortdirection=desc&q=", keywords, "%20")

        # extract stories to crawl
        for article in soup.find_all("div", {"class": "story"}):
            url = "https://www.thestar.com" + article.find_all("a")[0]["href"]
            try:
                img_url = "https://www.thestar.com" + article.find_all("img")[0]["src"]
            except:
                img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM8uGLeO03VvFX8zhIAQMxpZCNL9K5w1bgDurygXMQknA8qcw5RQ"
            title = article.find_all("a")[1].get_text()
            article_data.append({"url": url, "img_url": img_url, "title": title})


        article_data = filter( lambda x : _relevent_date_star(x,date) , article_data)

    elif site == "torontosun":
        print("bilbo")
        soup = _get_search_html("https://torontosun.com/?s=", keywords, "+")
        # print(soup.prettify())

        # extract stories to crawl
        for article in soup.find_all('article'):

            url = article.contents[1].contents[1].get('href')
            img_url = article.contents[1].contents[1].contents[1]["src"]
            title = article.find_all("h4")[0].get_text()
            article_data.append({"url": url, "img_url": img_url, "title": title})


        for x in article_data: print (x)
        article_data = filter( lambda x : _relevent_date_sun(x,date) , article_data)


    else:
        print("error: this website is not supported")
        exit(1)

    return article_data

if __name__== '__main__':
    find_related_articles(["climate", "change"], "toronto star")