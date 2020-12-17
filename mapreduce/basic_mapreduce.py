def mapper(s): # string -> [(key value)]
    pairs = []
    for c in s:
        pairs.append((c,1))
    return pairs
    
def combiner(pairs):
    index = {}
    for (key,value) in pairs:
        if key not in index:
            index[key] = [value]
        else:
            index[key].append(value)
    print(index)
    pairs = []
    for key in index:
        pairs.append((key,index[key]))
    return pairs
    
def reducer(pairs):
    output_pairs = []
    for key, value in pairs:
        reduced_value = sum(value)
        output_pairs.append((key,reduced_value))
    return output_pairs
    
if __name__ == "__main__":
    pairs = mapper("hello")
    print(pairs)
    pairs = combiner(pairs)
    print(pairs)
    pairs = reducer(pairs)
    print(pairs)
