from mapreduce import MapReduce

class CharCount(MapReduce):

    def mapper(self, _, line):
        for char in line:
            yield (char,1)

    def reducer(self, key, values):
        yield key, sum(values)

input = [
    "hello"
    ]

charCount = CharCount()
output = charCount.run(input)
for item in output:
    print(item)