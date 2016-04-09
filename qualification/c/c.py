#!/usr/bin/env python

import numpy
import sys

from math import sqrt

num_base_cache = {}

def solve(fname):
  with open(fname) as f:
    f.readline()
    cur_case = 1

    for line in f:
      length, count = map(int, line.split(' '))

      start = eval('0b1{}'.format('0' * (length - 1)))
      end = eval('0b{}'.format('1' * (length))) + 1

      print 'Case #{}:'.format(cur_case)

      while start < end:
        if not is_jamcoin(start):
          start += 1
          continue

        bin_j = bin(start)[2:]
        factors = []

        for base in xrange(2, 11):
          base10_num = to_base_10(bin_j, base)
          factors.append(str(first_factor(base10_num)))

        print '{} {}'.format(bin_j, ' '.join(factors))

        count -= 1
        start += 1

        if count <= 0:
          break

def is_jamcoin(num):
  str_rep = bin(num)[2:]

  if str_rep[-1] == '0':
    return False

  for base in xrange(2, 11):
    if isprime(to_base_10(str_rep, base)):
      return False

  return True

def first_factor(n):
    for i in xrange(2, 100000000):
      if n % i == 0:
        return i

def cache_prime(func):
  prime_table = {}

  def wrapper(n):
    if n not in prime_table:
      prime_table[n] = func(n)
    return prime_table[n]

  return wrapper

@cache_prime
def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= 100000000:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def to_base_10(n, base):
  if (n, base) in num_base_cache:
    return num_base_cache[(n, base)]

  n = n[::-1]
  num = 0

  for e in xrange(0, len(n)):
    num += int(n[e]) * base ** int(e)

  num_base_cache[(n, base)] = num

  return num

def check(fname):
  with open(fname) as f:
    f.readline()

    for line in f:
      num = line.split(' ')[0]

      for base in xrange(2, 11):
        if isprime(to_base_10(num, base)):
          print 'fucked!'

if __name__ == '__main__':
  solve(sys.argv[1])
