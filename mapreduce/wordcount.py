#!/usr/local/bin/python3.8

from mapreduce import MapReduce
from collections import Counter

class WordCount(MapReduce):

    def mapper(self, _, line):
        for word in line.split(" "):
            yield (word.strip(),1)

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


import re
top_Words = re.findall(r'\w+', open('alice.txt').read().lower())
def most_frequent(top_Words):
    least_count = Counter(top_Words).most_common()[:-10-1:-1]
    most_count = Counter(top_Words).most_common(10)
    print("Top 10 most occuring words", most_count)
    print("Least 10  occuring words", least_count)


a= most_frequent(top_Words)