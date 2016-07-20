from textblob import TextBlob
from textblob.tokenizers import WordTokenizer
from lexicons.behavior_lexicon import *
from lexicons.domain_lexicon import *


class Msg:

    def __init__(self, text):
        self.text = text
        self.words = None
        self.word_count = 0
        self.sentiments = list()
        self.behaviors = list()
        self.domains = list()
        self.analyze = Analyze()

        self.tokenize_text(self.text)
        self.add_msg_sentiment(self.analyze.analyze_sentiment(self.text))

    def tokenize_text(self, block):
        tokenizer = WordTokenizer()
        token = tokenizer.tokenize(block)
        self.words = token
        self.word_count = len(token)

    def add_msg_sentiment(self, new_sentiment):
        self.sentiments.append(new_sentiment)

    def add_msg_behavior(self, new_behavior):
        self.behaviors.append(new_behavior)

    def add_msg_domain(self, new_domain):
        self.domains.append(new_domain)


class Analyze:

    def analyze_sentiment(self, text):
        return TextBlob(text).sentiment

    def analyze_behavior(self, word_list):

        resultList = list()

        for word in word_list:
            for key in behaviorDict:
                if word in key:
                    resultList.append(behaviorDict[key])

        return resultList

    def analyze_domain(self, word_list):
        resultList = list()

        for word in word_list:
            for key in domainDict:
                if word in key:
                    resultList.append(domainDict[key])

        return resultList
