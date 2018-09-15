####################################################################################
# Utility Functions that extract and calculate keywords
####################################################################################
import nltk
from nltk.corpus import stopwords

# Constant
stop_words = set(stopwords.words('english'))


####################################################################################
# keywordsInDoc  
#   Description: 
#     Extract caller specified number of top keywords that has the highest relavency 
#     score in the document using a modified TF-IDF algorithm
#   Input:
#     string_block
#       The character string that contain the document
#   Output:
#     dictionary of keywords with scores
####################################################################################
def keywordsInDoc(string_block,numKw):
    # error handelling
    if not isinstance(string_block, str) or not isinstance(numKw,int):
        raise valueError("keywordsInDoc: ERROR! pass in variables type is incorrect")
    # empty document
    if string_block is None:
        return None

    # Document parse
    # --------------------------------------------------------------
    word_list = string_block.split()
    word_list = [''.join(filter(str.isalnum, x)) for x in word_list] 
    # Generate unique list of words and remove stop word
    uniq_list = [w for w in list(set(word_list)) if not w in stop_words] 
    # return word with equal score if number of unique word is less than the 
    # specified number of keywords
    if len(uniq_list) < numKw:
        word_score = {(k,1) for k in uniq_list}
        return word_score

    
    # Calculate TF-IDF score for all unique words
    # --------------------------------------------------------------
    # TF score
    word_freq = {(k,word_list.count(k)) for k in uniq_list}
    tf_score = {(k,word_freq[k]/len(word_list)) for k in uniq_list}
    # IDF score
    sentences = string_block.splitlines()
    word_occurance = {}
    for s in sentences:
        # Get a list of all words in the sentence without special characters
        words = s.split()
        words = [''.join(filter(str.isalnum, w)) for w in s]
        for w in words:
            if (w in word_occurance): 
                word_occurance[w] += 1
            else:
                word_occurance[w] = 1
    idf_score = {(k, log(word_occurance[k]/len(sentences))) for k in uniq_list}
    # TF-IDF score
    word_score = {(k,tf_score[k] * idf_score[k]) for k in uniq_list}

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
    
    return result



####################################################################################
# get_keywords_to_crawl  
#   Description: 
#     Ratio out the balance between relevant words in the ariticle and the title 
#   Input:
#     string_block
#       The character string that contain the document
#   Output:
#     dictionary of keywords with scores
####################################################################################
def get_keywords_to_crawl(title, relavent_words):
    # error handelling
    if not isinstance(title, str) or not isinstance(relavent_words,dict):
        raise valueError("get_keywords_to_crawl: ERROR! pass in variables type is incorrect")
    # empty string or relavent words
    if relavent_words is None:
        return [''.join(filter(str.isalnum, x)) for x in title.split()] 
    elif title is None:
        return relavent_words.keys()
    else:
        return None
    # compare the word list and the words in title
    # TODO: get the ratio
    # TODO: compare to the library output

        

