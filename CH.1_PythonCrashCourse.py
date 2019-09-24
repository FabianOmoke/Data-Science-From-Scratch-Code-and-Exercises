
##THIS ARE RANDOM NOTES I WROTE IN CH.1 CRASH COURSE IN PYTHON
from collections import defaultdict as dd,Counter
import random

tweet = {    "user" : "joelgrus",
             "text" : "Data Science is Awesome",
             "retweet_count" : 100,
             "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
        }

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

name = "Usilete compe kwanza kwa manzi yangu manze"

d = {}

for c in name:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

print(d, end="\n")

e = dd(int)

for c in name:
    e[c] += 1
print(e)

c = Counter(name)

for i, count in c.most_common(3):
    print(i,count)

print(c)

x=25

parity = "even" if x % 2 == 0 else "odd"

print(parity)

y = None

assert y is None, "NO IT IS NOT"

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

numbers_toTen = [i for i in range(11)]

choose = random.choice(numbers_toTen)

random.shuffle(numbers_toTen)

sample = random.sample(numbers_toTen, 5)

print(choose)
print(numbers_toTen)
print(sample)


values: list[int]= []
