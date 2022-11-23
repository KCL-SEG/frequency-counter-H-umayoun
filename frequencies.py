"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(0, len(items)):
        item = str(items[i])
        if frequencies.get(item) is None:
            frequencies[item] = 1
            i = i+1
        else:
            frequencies[item] = frequencies.get(item) + 1
            i = i+1
    
    print(frequencies)


    return frequencies

frequencies([1,2,3,4,4,4,4, 'Hello', 'Hello'])


