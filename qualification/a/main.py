#!/usr/bin/env python

import sys

def solve(fname):
  with open(fname) as f:
    f.readline()
    cur_case = 1

    for line in f:
      line = line.rstrip('\n')
      start_num = int(line)
      cur_factor = 2

      seen_nums = { start_num: True }
      seen_digits = {}

      map(lambda x: add_digits(seen_digits, x), line)

      while True:
        cur_num = start_num * cur_factor

        map(lambda x: add_digits(seen_digits, x), str(cur_num))

        if len(seen_digits) == 10:
          print 'Case #{0}: {1}'.format(cur_case, cur_num)
          break
        elif cur_num in seen_nums:
          print 'Case #{0}: {1}'.format(cur_case, 'INSOMNIA')
          break
        else:
          seen_nums[cur_num] = True
          cur_factor += 1

      cur_case += 1

def add_digits(hash_table, key):
  hash_table[key] = True

if __name__ == '__main__':
  solve(sys.argv[1])
