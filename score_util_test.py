import score_util

article_set = [
"hi",
"I am a really short article",
""" 
Updated 5:47 PM ET, Fri September 14, 2018
Editor's Note: Andre Spicer is a professor of organizational behavior at Cass Business School, City, University of London. He and Carl Cederstrom are co-authors of "The Wellness Syndrome" and "Desperately Seeking Self-Improvement." The opinions expressed in this commentary are solely those of the author. View more opinion articles on CNN.

(CNN) - It's the end of the internet as we know it. At least that's what some say about new copyright legislation working its way through the European Parliament in Brussels. But behind all the talk about censorship machines and the death of memes is another much more fundamental issue -- the power of big tech companies.

The copyright legislation was designed to update European copyright law to reflect the challenges of a digital world.

Indeed, the debate around the European copyright directive is really about who profits from what is circulated on the internet. Should it be the big platform companies like Google and Facebook that have created new ways of distributing content and built up gigantic advertising business in the process? Or should it be "legacy" media firms like newspapers and TV networks that still create a lot of content?

Three parts of the regulation have proved controversial.

Article 3 would limit companies' ability to data-mine texts. Research organizations could use algorithms to mine texts, but in some cases firms would need a license to do the same thing.

Article 11 of the directive would require content-aggregation sites to pay content owners for the headlines they use to link to an original article on another site. For instance, Google News would need to pay The Guardian for using a headline that links through to an article on The Guardian's website.

Article 13 of the directive puts the onus on large tech firms to get the agreement of copyright holders when sharing content on their sites. For instance, Facebook would have to make sure an image shared by a user is not under copyright.

The new legislation has sparked outcries in the tech community. In an open letter to the European Parliament, 70 public figures, including Tim Berners-Lee (inventor of the World Wide Web) , warned that it could transform "the Internet from an open platform for sharing and innovation, into a tool for the automated surveillance and control of its users."

Intellectual property rights experts also claimed that changes to the legislation will create more problems than they solve.

Some corners of the internet have been flooded with talk about "memes bans," "link taxes" and "censorship machines." Opponents of the directive have pointed out the role of "legacy" media outfits, like the German media conglomerate Alex Springer, in promoting the law.

Behind the outrage is the tale of big tech companies confronting legislative changes that are a fundamental challenge to their business model. And, to avoid having to transform it, the companies are trying to use significant political power.

Each of the changes in European legislation create a big problem for those business models. Article 3 would put the brakes on big business opportunities for these companies in text mining and artificial intelligence. Article 11 represents an attack on the huge business big tech firms have built by selling advertising placed next to content others have produced. Article 13 would make it much harder for big tech firms to benefit from content produced by others while not having to pay those who produced it.

The new legislation could mean lower growth opportunities, more cost and less profit for these big tech companies. According to one estimate, Google has spent about 31 million euros lobbying Europe in recent years.

This has been both through direct lobbying (which it spent over 5 million euros on in 2016 alone), as well as indirect lobbying undertaken by the 24 lobbying organizations in Brussels it regularly funds. Bureaucrats working in the European Commission have declared the amount of lobbying from both sides of the argument "astonishing."

There is a big chance that as big tech battles it out with legacy media in a lobby war in Brussels, the one group that will lose out are the people who actually create the photos, songs and texts we share every day, and are unrewarded. What about them?
"""
]

for article in article_set:
    l = keywordsInDoc(article, 3)
    print (l)