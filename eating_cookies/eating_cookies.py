#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n == 0: return 0
    if n == 1: return 1

    return eating_cookies(n-1) + eating_cookies(n-2)

cache = {
    0: 0,
    1: 1
}

def cookie_cache(n):
    global cache

    if n in cache:
        return cache[n]

    cache[n] = cookie_cache(n-1) + cookie_cache(n-2)

    return cache[n]



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')