import os
import time
from collections import defaultdict
from collections import deque
from functools import reduce
from operator import mul
import sys
import re
import itertools


class Node:
    def __init__(self,v):
        self.v = v
        self.next = None

class circList:
    def __init__(self,cups,part2 = False):
        self.p2size = 1000000
        self.head = Node(int(cups[0]))
        
        self.size = len(cups)
        if part2:
            self.size = self.p2size
        prev = self.head
        for i in range(1,len(cups)):
            newNode = Node(int(cups[i]))
            if not part2:
                if i == len(cups) - 1:
                    newNode.next = self.head
            prev.next = newNode
            prev = newNode
        
        if part2:
            for i in range(len(cups)+1,self.p2size+1):
                newNode = Node(i)
                if i == self.p2size:
                    newNode.next = self.head
                prev.next = newNode
                prev = newNode
        self.lookup = dict()
        self.lookup[self.head.v] = self.head
        curr = self.head.next
        while curr != self.head:
            self.lookup[curr.v] = curr
            curr = curr.next

    def print(self):
        curr = self.head
        print(curr.v,sep=',',end=',')
        curr = curr.next
        #cnt = 0
        while curr != self.head:
        #while cnt < self.size:
            print(curr.v,sep=',',end=',')
            curr = curr.next
            #cnt += 1
        print()
    def stepN(self,n):
        if n == 0:
            return
        if n < 0:
            n = self.size + n
        n %= self.size
        for _ in range(n):
            self.head = self.head.next
    
    def printP1(self):
        curr = self.head
        outputOrder = []
        while curr.v != 1:
            curr = curr.next
        curr = curr.next
        while curr.v != 1:
            outputOrder.append(curr.v)
            curr = curr.next
        outputString = "".join(map(str,outputOrder))
        print("P1:",outputString)
    def printP2(self):
        curr = self.head
        while curr.v != 1:
            curr = curr.next
        print("P2:", curr.next.v,curr.next.next.v)
    def play1(self):
        # pickup 3 nodes
        # print("1",end="")
        p1 = self.head
        p2 = self.head.next
        p3 = (p2.next).next
        p4 = p3.next
        # print("2",end="")
        # print("play nodes",p1.v,p2.v,p3.v,p4.v)
        # compute destination
        tmpValues = set([p2.v,p2.next.v,p3.v])
        ## TODO no set, just compare
        # print(tmpValues)
        # print("3",end="")
        destValue = self.head.v-1
        if destValue == 0:
            destValue = self.size
        # if destValue in tmpValues:
        #     destValue = min(tmpValues)-1
        #     if destValue == 0:
        #         destValue = 9
        while destValue in tmpValues:
            destValue -= 1
            if destValue == 0:
                destValue = self.size
        # print("4",end="")
        # print(destValue)
        # remove from circle
        p1.next = p4
        # find place to insert
        # curr = self.head
        # while curr.v != destValue:
        #     curr = curr.next
        curr = self.lookup[destValue]
        # print("I am here:", curr.v,curr.next.v)
        pp1 = curr
        pp2 = curr.next
        pp1.next = p2
        p3.next = pp2
        # self.stepN(1)
        self.head = self.head.next
        # print()
        

def solve(n):
    
    s = '247819356'
    cups = [int(x) for x in s]
    ext = [x for x in range(10, n+1)]
    cups += ext

    d = {}
    for i in range(len(cups)):
        if i == len(cups)-1:
            d[cups[i]] = cups[0]
        else:
            d[cups[i]] = cups[i+1]

    start = int(s[0])
    for i in range((n*10)+1):
        a = d[start]
        b = d[a]
        c = d[b]
        d[start] = d[c]
        put = start-1
        if put in [a,b,c] or put < 1:
            while put in [a,b,c] or put < 1:
                put -=1
                if put < 1:
                    put = n
        d[c] = d[put]
        d[put] = a
        start = d[start]

    return d[1] * d[d[1]]


def main():

    # input
    print(os.getcwd())
    print(sys.version)
    day = "23"
    part1, part2 = 0, 0
    star_line = "*" * 19
    inputFile = f'inputs/input{day}.txt'
    start_time = time.time()
    # f = open(inputFile).read()
    input = "247819356"
    circ = circList(input,True)
    for i in range(10000000):
        circ.play1()
        # print(i)
        # circ.print()
    circ.printP2()

    # circ2 = circList("389125467",True)
    # # circ2.print()
    # # circ2.stepN(1)
    # # circ2.print()
    # # circ2.printP2()
    # for i in range(1000000):
    #     circ2.play1()
    # circ2.printP2()
    # print(solve(1000000))
    # circ.print()
    # circ.stepN(9)
    # circ.print()
    # circ.printP1()
    # circ.play1()
    # circ.print()
    duration = int((time.time() - start_time) * 1000)
    print(
        f"\n{star_line}\n AoC 2020 - Day {day}\n{star_line}\n\nPart 1:\t\t{part1}\nPart 2:\t\t{part2}\nDuration:\t{duration} ms")


if __name__ == "__main__":
    main()
