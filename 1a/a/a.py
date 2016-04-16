#!/usr/bin/env python

import sys

def solve(fname):
  with open(fname) as f:
    f.readline()
    cur_case = 1

    for line in f:
      line = line.rstrip('\n')
      biggest = line[0]
      answer = ''

      for char in line:
        if char >= biggest:
          answer = char + answer
          biggest = char
        else:
          answer = answer + char

      print 'Case #{}: {}'.format(cur_case, answer)
      cur_case += 1

if __name__ == '__main__':
  solve(sys.argv[1])
