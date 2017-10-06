#!/usr/bin/python

from collections import defaultdict
import sys

def diff(a, b):
    return sum(x != y for x,y in zip(a, b))

def make_graph(words):
    graph = {}
    for word in words:
        graph[word] = []
        for i, c in enumerate(word):
            for newc in "abcdefghijklmnopqrstuvwxyz":
                if c == newc: continue
                newword = word[:i] + str(newc) + word[i+1:]
                if newword in words:
                    graph[word].append(newword)
    return graph

def path(graph, start, end):
    visit = [start]
    seen = set([start])
    parent = {}
    while visit:
        node = visit.pop(0)
        if node == end: break
        for child in graph[node]:
            if child not in seen:
                seen.add(child)
                parent[child] = node
                visit.append(child)
    ans = [end]
    while end != start:
        end = parent[end]
        if end in ans: return []
        ans.append(end)
    return ans[::-1]

words = defaultdict(set)

with open("/usr/share/dict/words") as f:
    for line in f:
        words[len(line.strip())].add(line.strip().lower())

a = sys.argv[1]
b = sys.argv[2]

if len(a) != len(b):
    print "Not Possible"
    exit(1)

possibs = words[len(a)]
graph = make_graph(possibs)

print path(graph, a, b)

