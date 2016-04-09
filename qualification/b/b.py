#!/usr/bin/env python

import pprint
import sys

def solve(fname):
  with open(fname) as f:
    f.readline()
    cur_case = 1

    for line in f:
      existing_sol = {
        '+': 0,
        '+-': 2,
        '-': 1,
        '-+': 1,
      }

      reduced_line = reduce_str(line.rstrip('\n'))

      calc(reduced_line, existing_sol)

      print 'Case #{}: {}'.format(
        cur_case,
        existing_sol[reduced_line]
      )

      cur_case += 1


def calc(conf, existing_sol):
  if conf in existing_sol:
    return existing_sol[conf]

  flips = 1
  flip_reduced = reduce_str(flip(conf))

  while flip_reduced not in existing_sol:
    flip_reduced = reduce_str(flip(flip_reduced))
    flips += 1

  existing_sol[conf] = existing_sol[flip_reduced] + flips
  return existing_sol[conf]

def flip(conf, index=0):
  return ''.join(map(
    lambda x: '-' if x == '+' else '+',
    conf[:index + 1][::-1]
  )) + conf[index + 1:]

def reduce_str(conf):
  if (len(conf)) < 1:
    raise Exception('shit')

  if len(conf) == 1:
    return conf

  start = 0
  reduced_conf = conf[0]

  for dup_end in xrange(1, len(conf)):
    if conf[dup_end] != reduced_conf[-1]:
      reduced_conf = reduced_conf + conf[dup_end]

  return reduced_conf

if __name__ == '__main__':
  solve(sys.argv[1])
