#!/usr/bin/env python

import re

BCP_FILE = "src/bcp11.txt";

RE_PAGE = "^<page (?P<pageNumber>\d+)>"

PAGE_COUNTER = 0

def checkPageNumber(line):
  match = re.search(RE_PAGE, line)
  # match returns None (falsy) or MatchObject (truthy)
  if match: 
    global PAGE_COUNTER
    PAGE_COUNTER = int(PAGE_COUNTER) + 1
    thisPage = int(match.group('pageNumber'))
    if thisPage > PAGE_COUNTER:
      print "checkPageNumber: missing page {0} - {1})".format(PAGE_COUNTER, thisPage-1)
      PAGE_COUNTER = thisPage
    if thisPage < PAGE_COUNTER:
      print "checkPageNumber: duplicate/out of order page: {0}".format(PAGE_COUNTER)

def main():

  with open(BCP_FILE, 'r') as bcp:
    for line in bcp:
      checkPageNumber(line)


if __name__ == "__main__":
  main()
