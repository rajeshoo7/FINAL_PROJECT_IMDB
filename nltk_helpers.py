# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def get_sentiments(text):
    
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text) 




def split_sentiments(sentiments):
    xs = [sent['neg'] for sent in sentiments]
    ys = [sent['neu'] for sent in sentiments]
    zs = [sent['pos'] for sent in sentiments]
    
    return xs,ys,zs