"""
Determine repeated probabilities.

Author: Peter Gow
Python 3.7
"""

# define constants
number = 3


def find_sum(probs={0: 1}, target=False, n=number, norm=True, display=True):
    """Find the probability sums of a set of probabilities."""
    setsum = sum(probs.values())
    for i, j in probs.items():
        probs[i] = j/setsum
    newprobs = {}
    if n > 1:
        for i, j in probs.items():
            for k, l in find_sum(probs=probs, n=n-1, display=False).items():
                newprobs[i+k] = newprobs.get(i+k, 0) + j*l
    else:
        newprobs = probs
    if display:
        for i, j in newprobs.items():
            print(str(i) + ":", str(j*100) + "%", sep="\t\t")
    return newprobs


testing = False
if __name__ == "__main__" and testing:
    # Change the probabilities here:
    probs = {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1
    }
    res = find_sum(probs=probs, n=2)
