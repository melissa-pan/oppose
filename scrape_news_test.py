from news_scraper import news_scrape

def runme():
	articles = ["https://www.thestar.com/entertainment/visualarts/2018/09/15/the-mystery-of-flavio-da-silva-povertys-poster-child.html",
	"https://www.thestar.com/news/queenspark/2018/09/15/tories-to-hold-midnight-session-to-ram-through-controversial-bill-that-would-slash-the-size-of-toronto-council.html",
	"https://torontosun.com/news/provincial/midnight-debate-scheduled-for-bill-31-on-monday"]
	for article in articles:
		l = news_scrape(article,3)
		print (l)

if __name__ == "__main__":
    runme()



