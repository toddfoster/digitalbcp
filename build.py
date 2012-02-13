#!/usr/bin/env python

import re

OUTPUT_FILE = "index.html";
BOILERPLATE_FILE = "src/index.html"
BOILERPLATE_MAIN= '<div role="main">';
BCP_FILE = "src/bcp10.txt";

RE_PAGE = "^<[Pp]age (?P<pageNumber>\d+)>"

def getBoilerplateBeforeMain(f):
  with open(BOILERPLATE_FILE, 'r') as b:
    for line in b:
      # TODO: modify headers, title, etc.
      f.write(line)
      if BOILERPLATE_MAIN in line:
        break


def getBoilerplateAfterMain(f):
  with open(BOILERPLATE_FILE, 'r') as b:
    line = b.readline()
    while not BOILERPLATE_MAIN in line:
      line = b.readline()
    for line in b:
      f.write(line)

def findPageNumber(f, line):
  match = re.search(RE_PAGE, line)
  # match returns None (falsy) or MatchObject (truthy)
  if match:
    f.write('<p class="bcp_page_number">{0}</p>\n'.format(int(match.group('pageNumber')) - 1))
    f.write('</div>\n\n')
    f.write('<div class="bcp_page" id="page{0}">\n'.format(match.group('pageNumber')))
  return match

def addNavigationBar(f):
  f.write('<input type="submit" name="navigateLeft" value="Navigate Left" id="navigateLeft" />')
  f.write('<div id="navigationInfo"></div>')
  f.write('<input type="submit" name="navigateRight" value="Navigate Right" id="navigateRight" />')

def scrub(line):
  return line.translate(None, "<>")

def main():
  # TODO: Check for existence of input files

  with open(OUTPUT_FILE, 'w') as f:
    getBoilerplateBeforeMain(f)

    addNavigationBar(f)
    with open(BCP_FILE, 'r') as bcp:
      f.write('<div class="bcp_page" id="page0">')
      for line in bcp:
        if findPageNumber(f, line):
          continue
        line = scrub(line)
        f.write(line)
    f.write('</div>\n') # close last page
    addNavigationBar(f)
    getBoilerplateAfterMain(f)


if __name__ == "__main__":
    main()
