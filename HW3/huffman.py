#!/usr/bin/env python3
import sys
DEBUG = True
string = """honorificabilitudinitatibus"""


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s_%s" % (self.left, self.right)


## Tansverse the NodeTress in every possible way to get codings
def huffmanCodeTree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + "0"))
    d.update(huffmanCodeTree(r, False, binString + "1"))
    return d

if DEBUG:
    print("Input file: " + sys.argv[1])

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

#Sort the frequency table based on occurrence this will also convert the
#dict to a list of tuples
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if DEBUG:
    print(" Char | Freq ")
    for key, c in freq:
        print( " %4r | %d" % (key, c))

nodes = freq

while len(nodes) > 1:
    key1, c1 = nodes[-1]
    key2, c2 = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    # Re-sort the list
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

if DEBUG:
    print( "left: %s" % nodes[0][0].nodes()[0])
    print( "right: %s" % nodes[0][0].nodes()[1])

huffmanCode = huffmanCodeTree(nodes[0][0])

print( " Char | Freq  | Huffman code ")
print( "-----------------------------")
for char, frequency in freq:
    print( " %-4r | %5d | %12s" % (char, frequency, huffmanCode[char]))
