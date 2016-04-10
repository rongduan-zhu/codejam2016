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
      p, c, s = map(int, line.split(' '))

      print 'Case #{}: {}'.format(cur_case, ' '.join([str(i) for i in xrange(1, p + 1)]))
      cur_case += 1

def get_expanded_position(pattern, complexity, position):
  if complexity <= 1:
    return position

  return position + left_count(pattern, complexity - 1, position - 1) * pattern

def left_count(pattern, complexity, position):
  if complexity <= 1:
    return position

  return position + left_count(pattern, complexity - 1, position) * pattern

if __name__ == '__main__':
  solve(sys.argv[1])
