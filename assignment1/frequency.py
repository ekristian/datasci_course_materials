import sys
from tweetlib import get_tweets
from tweetlib import get_tweet_text
from tweetlib import get_words



def main():
    tweet_file = sys.argv[1]
    freq = {}
    total_terms = 0.0
    hist = {}
    for tweet in get_tweets(tweet_file):
        for w in get_words(get_tweet_text(tweet)):
            total_terms = total_terms + 1
            freq[w] = freq.get(w,0.0) + 1
    for k, v in freq.items():
        print "%0.6f %s" % (v/total_terms, k)


if __name__ == "__main__":
    main()

