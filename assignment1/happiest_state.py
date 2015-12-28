import sys
import json
import pprint

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


# get_sentiment_dict reads a file specified by <filename>.
# The expected line is a two field tab delimited record
# consiting of term and sentiment scores.
#
# Arguments:
#    filename - File containing term and sentiment values
#
# Returns:
#   sentiment - A python dictionary containing term/sentiment values
#
def get_sentiment_dict(filename):
    fp = open(filename)
    sentiment = {}
    for line in fp:
        key, value = line.split("\t")
        sentiment[key] = int(value)
    return sentiment


# get_tweets yields one JSON object representing a single tweet from
# the file specified by filename.  It will yield tweets until the file has been
# exhausted.
#
# Arguments:
#    filename - The file containing tweets in JSON format. One per line.
#
# Returns:
#    JSON object - A Python JSON object representing one tweet.
#
def get_tweets(filename):
    fp = open(filename)
    for line in fp:
        yield(json.loads(line))


# get_tweet_text returns the value associated with the text key found in the
# JSON object representing the tweet.
#
# Arguments:
#    tweet - A Python JSON object representing a tweet from the Twitter API.
#
# Returns:
#    text - A Python string object value from the text key.
#
def get_tweet_text(tweet):
    text = ""
    if u'text' in tweet:
        text = tweet[u'text'].encode("utf-8")
    return text


# get_words yields one word per tweet until all the words have been exhausted.
#
# Arguments:
#    text - A Python string containing the words to iterate.
#
# Returns:
#    string - a single word string.
#
def get_words(text):
    return [w.lower() for w in text.split()]


# get_term_sentiment returns the sentiment score from the sentiment dictionary
# if the term is not found in the dictionary a score of zero will be returned.
#
# Arguments:
#    sent_dict - A Python dictionary containing term/score name value pairs.
#    word - A Python string representing a single term.
#
# Returnds:
#    sentiment - the sentiment score found in the sent_dict dictionary;
#                otherwise 0.
#
def get_term_sentiment(sent_dict, word):
    sentiment = 0
    if word in sent_dict:
        sentiment = sent_dict[word]
    return sentiment


# get_tweet_sentiment adds all the sentiment scores for each term found in the
# tweet.
#
# Arguments:
#    sent_dict - A Python dict containing term/sentiment name/value pairs.
#
# Returns:
#    sentiment - Sum total of all sentiment scores found for each term in the
#                tweet.
#
def get_tweet_sentiment(sent_dict, tweet):
    sentiment = 0
    for word in get_words(get_tweet_text(tweet)):
        sentiment = sentiment + get_term_sentiment(sent_dict, word)
    return sentiment


# stream_tweet_sentiments yeilds one sentiment score per tweet found in the
# file specified by filename.
#
# Arguments:
#    sent_dict - A Python dict containing term/sentiment name/value pairs.
#    filename - A file containing tweets.
#
def stream_tweet_sentiments(sent_dict, filename):
    for tweet in get_tweets(filename):
        yield(get_tweet_sentiment(sent_dict, tweet))


def known_term(sent_dict, term):
    return term in sent_dict


def unknown_term(sent_dict, term):
    return not(known_term(sent_dict, term))


def get_unknown_terms(sent_dict, text):
    return [w for w in get_words(text) if unknown_term(sent_dict, w)]


def get_location(tweet):
    retval = ""
    if u'user' in tweet:
        user = tweet[u'user']
        if u'location' in user:
            location = user[u'location']
            if location is not None:
                retval = location.encode("utf-8").lower()
    return retval


def get_state(tweet, state_dict):
    location = get_location(tweet)
    for word in get_words(location.translate(None, ".,-")):
        if word in state_dict:
            return state_dict[word]


def master_lookup(state_dict):
    master_list = {}
    for k, v in state_dict.items():
        master_list[k.lower()] = k.lower()
        master_list[v.lower()] = k.lower()
    return master_list


if __name__ == '__main__':
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    sent_dict = get_sentiment_dict(sent_file)
    state_lookup = master_lookup(states)
    happy = {}
    for tweet in get_tweets(tweet_file):
        state = get_state(tweet, state_lookup)
        if state is not None:
            happy[state] = happy.get(state, 0) + get_tweet_sentiment(
                                                    sent_dict, tweet)
    counter = 1
    for k, v in sorted(happy.iteritems(), key=lambda(k, v): (v*-1, k)):
        if counter > 0:
            print k.upper()
        counter = counter - 1
