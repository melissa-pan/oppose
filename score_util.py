####################################################################################
# Utility Functions that extract and calculate keywords
####################################################################################
import nltk
import math
from nltk.corpus import stopwords

# Constant
stop_words = set(stopwords.words('english'))
my_stop_words = ['']
stop_words = set(list(stop_words) + my_stop_words)

# Finds keywords in a block of string using the idea of tf-idf algorithm
def keywordsInDoc(string_block,numKw):
    """
    Description: 
        Extract caller specified number of top keywords that has the highest relavency 
        score in the document using a modified TF-IDF algorithm
    Input:
        string_block
        The character string that contain the document
    Output:
        dictionary of keywords with scores
    """
    # error handelling
    if not isinstance(string_block, str) or not isinstance(numKw,int):
        raise valueError("keywordsInDoc: ERROR! pass in variables type is incorrect")
    # empty document
    if string_block is None:
        return None

    # # Debug message 
    # print("starting to generate {} keywords in string block: \n {} \n".format(numKw, string_block))

    # Document parse
    # --------------------------------------------------------------
    string_block = string_block.lower()
    word_list = string_block.split()
    word_list = [''.join(filter(str.isalnum, x)) for x in word_list] 
    # Generate unique list of words and remove stop word
    uniq_list = [w for w in list(set(word_list)) if not w in stop_words] 
    # # Debug message
    # print("word list is: {}\n".format(word_list))
    # print("unique word is: {}\n".format(uniq_list))

    # return word with equal score if number of unique word is less than the 
    # specified number of keywords
    if len(uniq_list) < numKw:
        word_score = {k : 1 for k in uniq_list}
        return word_score
    
    # Calculate TF-IDF score for all unique words
    # --------------------------------------------------------------
    # TF score
    word_freq = {k : word_list.count(k) for k in uniq_list}
    tf_score = {k : word_freq[k]/len(word_list) for k in uniq_list}
    # print ("word score is: {}".format(tf_score))

    # IDF score
    sentences = string_block.splitlines()
    word_occurance = {}
    for s in sentences:
        # Get a list of all words in the sentence without special characters
        words = s.split(' ')
        words = [''.join(filter(str.isalnum, w)) for w in words]
        for w in words:
            if (w in word_occurance): 
                word_occurance[w] += 1
            else:
                word_occurance[w] = 1
    idf_score = {k : math.log(word_occurance[k]/len(sentences)) for k in uniq_list}
    # TF-IDF score
    word_score = {k : tf_score[k] * idf_score[k] for k in uniq_list}

    # Return top X number of keywords
    # -------------------------------------------------------------
    topXwords = sorted(word_score, key=word_score.__getitem__)
    topXwords.reverse()
    
    result = topXwords[:numKw]
    for w in topXwords[numKw:]:
        if word_score[w] == topXwords[numKw]:
            result.append(w)
        else:
            break
    
    word_score = {k : tf_score[k] * idf_score[k] for k in uniq_list}
    return result
    # return {k:v for (k,v) in word_score.items() if k is in result}


# scoring system between three source of potential keyword
def get_keywords_to_crawl(title, relavent_words, nlp_keyword, numKw):
    """
    Description: 
        Ratio out the balance between relevant words in the ariticle and the title.
        score system -- title weights 60%, nlp keywords weights 30%, tfidf weights 10%
    Input:
        title - title of the article
        relavent_words - the list of words found by our tf-idf algorithm
        nlp_keyword - the list of words found by newspaper library
        numKw - number of top score keyword to output
    Output:
        list of top keywords to query in opposing site
    """
    # error handelling
    if not isinstance(title, str) or not isinstance(relavent_words,list) or not isinstance(nlp_keyword,list):
        raise valueError("get_keywords_to_crawl: ERROR! pass in variables type is incorrect")
    
    print ("My pass in variable is {}, {}, {}, {}\n".format(title,relavent_words,nlp_keyword, numKw))

    # parse title 
    title_words = [''.join(filter(str.isalnum, x)) for x in title.lower().split() if x not in stop_words]

    # keyword pool for potential outputs
    keyword_pool = title_words + relavent_words + nlp_keyword

    # calculate each single source of keywords
    title_score = {k: 1 for k in title_words} 
    title_score.update({k: 0 for k in keyword_pool if k not in title_words}) 

    relavent_word_score = {k: (relavent_words[::-1].index(k) + 1) / len(relavent_words) for k in relavent_words}
    relavent_word_score.update({k: 0 for k in keyword_pool if k not in relavent_words}) 

    nlp_keyword_score = {k: (nlp_keyword[::-1].index(k) + 1) / len(nlp_keyword) for k in nlp_keyword}
    nlp_keyword_score.update({k: 0 for k in keyword_pool if k not in nlp_keyword})

    # use the pre-defined ratio to get the keywords with the highest number of score
    keyword_score = {k: title_score[k] * 0.8 + relavent_word_score[k] * 0.3 + nlp_keyword_score[k] * 0.1 for k in relavent_words}
    ranked_keyword = sorted(keyword_score, key=keyword_score.__getitem__)
    ranked_keyword.reverse()
   
    return ranked_keyword[:numKw]




        

