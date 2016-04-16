#!/usr/bin/env python

import sys
import copy

def solve(fname):
  with open(fname) as f:
    total_cases = int(f.readline())

    for cur_case in xrange(1, total_cases + 1):
      size = int(f.readline())

      nums = {}

      for i in xrange(0, 2 * size - 1):
        for num in map(int, f.readline().split(' ')):
          if num in nums:
            nums[num] += 1
          else:
            nums[num] = 1

      answer = []
      for key in nums:
        if nums[key] % 2:
          answer.append(key)

      print 'Case #{}: {}'.format(cur_case, ' '.join(map(str, sorted(answer))))


if __name__ == '__main__':
  solve(sys.argv[1])
