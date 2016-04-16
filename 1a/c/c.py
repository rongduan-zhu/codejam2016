#!/usr/bin/env python

import sys

class Node:
  def __init__(self, outgoing, incoming):
    self.outgoing = outgoing
    self.incoming = incoming

def solve(fname):
  with open(fname) as f:
    tests = int(f.readline())

    for i in xrange(tests):
      f.readline()

      deps = map(int, f.readline().split(' '))
      two_node_cycles = []
      nodes = {}

      for j in xrange(1, len(deps) + 1):
        # setup outgoing nodes
        if j in nodes:
          nodes[j].outgoing = deps[j - 1]
        else:
          nodes[j] = Node(deps[j - 1], [])

        # setup incoming nodes
        if deps[j - 1] in nodes:
          nodes[deps[j - 1]].incoming.append(j)
        else:
          nodes[deps[j - 1]] = Node(None, incoming=[j])

        # setup two node cycles
        if nodes[j].outgoing in nodes and j == nodes[nodes[j].outgoing].outgoing:
          two_node_cycles.append((j, nodes[j].outgoing))

      print 'Case #{}: {}'.format(i + 1, traverse(nodes, two_node_cycles))

def traverse(nodes, two_node_cycles):
  bff_cycle = 0
  visited = {}

  for n1, n2 in two_node_cycles:
    visited[n1] = True
    visited[n2] = True
    bff_cycle += traverse_up(n1, nodes, visited, 1)
    bff_cycle += traverse_up(n2, nodes, visited, 1)

  for node in nodes:
    if node not in visited:
      visited_in_path = set()
      visited_in_path.add(node)

      start = node
      current = nodes[start].outgoing
      longest_cycle = 1

      while current not in visited_in_path:
        visited_in_path.add(current)
        current = nodes[current].outgoing
        longest_cycle += 1

      if start == current and longest_cycle > bff_cycle:
        bff_cycle = longest_cycle

  return bff_cycle

def traverse_up(node, nodes, visited, length):
  max_len = length
  for up_node in nodes[node].incoming:
    if up_node not in visited:
      visited[up_node] = True
      up_length = traverse_up(up_node, nodes, visited, length + 1)

      max_len = up_length if up_length > max_len else max_len
  return max_len

if __name__ == '__main__':
  solve(sys.argv[1])
