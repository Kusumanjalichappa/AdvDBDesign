from mapreduce import MapReduce
from operator import itemgetter

class WordCount(MapReduce):
    def mapper(self, _, line):
        for word in line.split(" "):
            yield (word.strip(),1)

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


with open("alice.txt","r") as f:
    input = f.readlines()



output = WordCount().run(input)
max_key = ""
max_value = 0

lower_case = {}

for key,value in output:
     if(key.islower()):
         lower_case[key] =  value
res_most = dict(sorted(lower_case.items(), key = itemgetter(1), reverse = True)[:10])
res_least = dict(sorted(lower_case.items(), key = itemgetter(1), reverse = False)[:10])

print("10 Most common Non Captalized Words from alice.txt :",res_most)
print("10 lease common Non Captalized Words from alice.txt :",res_least)

