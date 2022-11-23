"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(0, len(items) - 1):
        if frequencies.get(items(i)) is None:
            frequencies[items(i)] = 1
            i = i+1
        else:
            frequencies[items(i)] = frequencies.get(items(i)) + 1
            i = i+1
        


    return frequencies
