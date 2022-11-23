"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(0, len(items) - 1):
        str = items(i).toString()
        if frequencies.get(str) is None:
            frequencies[str] = 1
            i = i+1
        else:
            frequencies[str] = frequencies.get(str) + 1
            i = i+1
        


    return frequencies
